from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.endpoints import blogs
from app.db import engine, metadata, database

metadata.create_all(engine)

app = FastAPI(title="FastAPI PostgreSQL CRUD App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def read_root():
    return {"message": "This is Python FastAPI blog application"}


app.include_router(blogs.router, prefix="/api/blogs", tags=["blogs"])