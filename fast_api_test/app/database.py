from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#postgresql-container
SQLALCHEMY_DATABASE_URL = "postgresql://test:test@postgresql-container/postgres"
#SQLALCHEMY_DATABASE_URL = "postgresql://test:test@localhost:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
