import fire
import json
import os
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import requests
from models import Document, Base

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432"
engine = create_engine(db_url)


def init_db():
    Base.metadata.create_all(engine)


class DataLoader:
    def load_seed_document_data(self):
        """Loads document data from a list of urls found in url_sources.json.
        """
        with open("url_sources.json", "r") as f:
            data = json.load(f)
            documents = []
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
                    except IntegrityError as e:
                        # TODO: Need to add some logging here.
                        print(e)


    def hello(self, greeting):
        """Make sure it's working."""
        
        print(f"Hello {greeting}!")

if __name__ == "__main__":
    fire.Fire(DataLoader)
