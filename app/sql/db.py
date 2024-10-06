from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

DATABASE_URI = settings.DATABASE_URI

# SQLAlchemy
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
