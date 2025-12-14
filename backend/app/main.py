from fastapi import FastAPI
from app.api import auth

app = FastAPI(title="Sweet Shop API")

app.include_router(auth.router)

@app.get("/health")
def health():
    return {"status": "ok"}
from app.api import auth, sweets

app.include_router(auth.router)
app.include_router(sweets.router)
