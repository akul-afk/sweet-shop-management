from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, sweets  
from app.db.database import engine
from app.db.base import Base  # 👈 IMPORTANT (loads models)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ CREATE TABLES
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(sweets.router)