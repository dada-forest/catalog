from fastapi import FastAPI
from datetime import datetime
import os
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, load_only

# from sentence_transformers import SentenceTransformer
import psycopg2
from models import Document

app = FastAPI(title="USFS Dada-Forest Metadata Catalog")

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432"
engine = create_engine(db_url)


@app.get("/health")
async def health():
    now = datetime.now()
    return {
        "msg": "ok",
        "data": now,
    }


@app.get("/documents")
async def documents():
    data = None
    with Session(engine) as session:
        documents = session.query(Document).options(
            load_only(
                Document.id, Document.identifier, Document.url, Document.description
            )
        )
        data = documents.all()

    return data


@app.get("/documents/search/{term}")
async def documents(term: str):
    """Simple query to see if search term is contained in a string field."""

    data = {"term": term}

    with Session(engine) as session:
        query = (
            session.query(Document)
            .options(
                load_only(
                    Document.id, Document.identifier, Document.url, Document.description
                )
            )
            .filter(Document.description.like(f"%{term}%"))
        )
        data["data"] = query.all()

    return data


# @app.get("/documents/vector/search/{term}")
# async def vector_seaarch_documents(term: str):
#     """Vector database search on a document description."""

#     resp = {"term": term}
#     model = SentenceTransformer("all-MiniLM-L6-v2")
#     embedding = model.encode(term).tolist()
#     embeddings = ",".join(str(e) for e in embedding)
#     embeddings = f"'[{embeddings}]'"
#     sql = f"""SELECT id, description, 1 - (embedding <=> {embeddings}) AS cosine_similarity FROM documents ORDER BY cosine_similarity DESC"""

#     documents = []
#     with psycopg2.connect(db_url) as conn:
#         with conn.cursor() as cursor:
#             cursor.execute(sql, embedding)
#             for row in cursor.fetchall():
#                 documents.append({
#                     "id": row[0],
#                     "description": row[1]
#                 })

#     resp["data"] = documents

#     return resp
