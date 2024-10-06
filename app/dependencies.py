from app.sql.db import SessionLocal


def get_db():
    """get db instance"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
