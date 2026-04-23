from database.models import create_tables
import uvicorn

if __name__ == "__main__":
    print("[DB] Creating tables...")
    create_tables()
    print("[DB] Tables ready ✔")

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)