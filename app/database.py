from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# For simplicity, we'll use SQLite. For production, use PostgreSQL!
# Using a relative path for the SQLite file
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# `check_same_thread` is only needed for SQLite to work with FastAPI's async nature
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Each instance of SessionLocal will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our ORM models
Base = declarative_base()
