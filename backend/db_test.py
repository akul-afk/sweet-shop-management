from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://sweet_user:Sweet123@localhost:3306/sweet_shop"
)

with engine.connect() as conn:
    result = conn.execute(text("SHOW TABLES"))
    print("Connected OK. Tables:", result.fetchall())
