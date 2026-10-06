from fastapi import FastAPI

from app.api import router
from app.db import Base, engine

app = FastAPI(title="FSP Career", version="0.1.0")


@app.on_event("startup")
def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


app.include_router(router, prefix="/api")
