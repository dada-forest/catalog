from sqlalchemy import Column, Integer, String, DateTime

# from pgvector.sqlalchemy import Vector
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship
from typing import Optional
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

Base = declarative_base()
target_metadata = Base.metadata
# N_DIM = 1536


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    identifier = Column(String(125), nullable=True, unique=True)
    url = Column(String(250), unique=False, nullable=True)
    description = Column(String(2500), unique=False, nullable=True)
    created_at = Column(
        TIMESTAMP(timezone="TRUE"), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone="TRUE"),
        nullable=False,
        server_default=text("now()"),
        server_onupdate=text("now()"),
    )
    # embedding = Vector(N_DIM)


class USFSNationalDataset(Base):
    __tablename__ = "usfs_national_dataset"

    id = Column(Integer, primary_key=True)
    title = Column(String(125), nullable=True, unique=True)
    metadata_url = Column(String(500), unique=True, nullable=True)
    description = Column(String(2500), unique=False, nullable=True)
    purpose = Column(String(500), unique=False, nullable=True)
    created_at = Column(
        TIMESTAMP(timezone="TRUE"), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone="TRUE"),
        nullable=False,
        server_default=text("now()"),
        server_onupdate=text("now()"),
    )
