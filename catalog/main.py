import os
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, load_only
from models import Document

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
db_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432"
engine = create_engine(db_url)

app = FastAPI(title="DADA-Forest API")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def index():
    return RedirectResponse("/docs")


@app.get("/health")
async def health():
    resp = {"msg": "ok", "data": datetime.now()}

    return resp


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
