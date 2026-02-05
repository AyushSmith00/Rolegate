from app.db.database import engine

try:
    with engine.connect() as conn:
        print("✅ PostgreSQL connected successfully")
except Exception as e:
    print("❌ Connection failed:", e)
