from fastapi import FastAPI
from app.db.session import engine

app = FastAPI(title="Sweet Shop API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    with engine.connect():
        return {"db": "connected"}

