from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:abhishek1234@localhost/Sociome'
engine=create_engine (SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(qutocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()