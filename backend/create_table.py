from app.db.database import engine, Base
import app.db.base  # 👈 forces model registration

print("Tables registered:", Base.metadata.tables.keys())
Base.metadata.create_all(bind=engine)
