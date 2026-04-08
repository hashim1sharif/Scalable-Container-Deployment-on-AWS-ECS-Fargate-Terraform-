import os
from dotenv import load_dotenv
from sqlalchemy import Column, DateTime, Integer, String, Table, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from databases import Database

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL)
Base = declarative_base()
metadata = MetaData()

blogs = Table(
    "blogs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(255)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

database = Database(DATABASE_URL)