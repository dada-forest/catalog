import os
import typer
from dotenv import dotenv_values
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, load_only, scoped_session, sessionmaker
from sentence_transformers import SentenceTransformer
import psycopg2

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

    model = SentenceTransformer("all-MiniLM-L6-v2")
    documents = _get_documents()
    with psycopg2.connect(db_url) as conn:
        with conn.cursor() as cursor:
            for doc in documents:
                id = doc[0]
                description = doc[2]
                embeddings = model.encode(description)
                sql = """UPDATE documents SET embedding = %s WHERE id = %s"""
                cursor.execute(sql, (embeddings.tolist(), id))
                

if __name__ == "__main__":
    app()