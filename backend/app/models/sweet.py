from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base   # ✅ SAME BASE

class Sweet(Base):
    __tablename__ = "sweets"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)
