from fastapi import FastAPI
from config import settings
from database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to Giglocal!"}