import os
import typer
from dotenv import dotenv_values
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, load_only, scoped_session, sessionmaker

config = dotenv_values("../.env")

POSTGRES_USER = config["POSTGRES_USER"]
POSTGRES_PASSWORD = config["POSTGRES_PASSWORD"]
POSTGRES_HOST = "localhost"
db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432"
engine = create_engine(db_url)

app = typer.Typer(no_args_is_help=True)

@app.command()
def hello():
    """Utility to test the cli."""
    print("Hello!")


def _get_documents() -> list:
    sql = text("select id, url, description from postgres.public.documents")
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()
    docs = session.execute(sql).fetchall()
    session.close()
    return docs if docs != None else []


@app.command()
def create_vector_data():
    """Create vector data for the document objects.
    """

    print("Creating Document vector data.")
    documents = _get_documents()
    print(documents)



if __name__ == "__main__":
    app()