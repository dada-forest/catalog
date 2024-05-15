import click
import json
import requests
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Document, Base
import os
from bs4 import BeautifulSoup

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432"
engine = create_engine(db_url)


@click.group()
def cli():
    pass


@click.command()
def load_seed_docs():
    print("Loading seed docs.")

    documents = []
    with open("doc_urls.json", "r") as f:
        data = json.load(f)
        for item in data:
            if item:
                url = item["url"]
                req = requests.get(url).json()
                if req:
                    identifier = req["identifier"]
                    description = req["description"]
                    document = Document(
                        identifier=identifier, url=url, description=description
                    )
                    documents.append(document)

    if documents and len(documents):
        with Session(engine) as session:
            session.add_all(documents)
            try:
                session.commit()
                print(f"Loaded {len(documents)} documents.")
            except IntegrityError as e:
                # TODO: Need to add some logging here.
                print(e)


@click.command()
def scrape_downloadable_national_datasets():
    metadata_hrefs = []
    base_url = "https://data.fs.usda.gov/geodata/edw/datasets.php"
    resp = requests.get(base_url)
    soup = BeautifulSoup(resp.content, "html.parser")
    table = soup.find("table", class_="fcTable")
    for i, row in enumerate(table.find_all("tr")):
        td = row.find("td", class_="metaLink") 
        if td:
            anchors = td.find_all("a")
            if anchors[0]["href"]:
                href = anchors[0]["href"]
                metadata_hrefs.append(href)
    print(metadata_hrefs)

if __name__ == "__main__":
    cli.add_command(load_seed_docs)
    cli.add_command(scrape_downloadable_national_datasets)
    cli()
