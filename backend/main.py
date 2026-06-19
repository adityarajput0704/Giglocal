from fastapi import FastAPI
from config import settings
from database import Base, engine
from routers import auth

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to Giglocal!"}

