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


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")
