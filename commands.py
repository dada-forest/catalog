import click
import json
import requests
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Document, Base
import os

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432"
engine = create_engine(db_url)


@click.group()
def cli():
    pass


@click.command("load_seed_docs")
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


if __name__ == "__main__":
    cli.add_command(load_seed_docs)
    cli()
