# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./PostJob.db'
SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://startup_787o_user:76ZNvMkzWIcDr73tXlTZLxUCwjOFe5S8@dpg-cmvrv7qcn0vc73aqnhpg-a.oregon-postgres.render.com/startup_787o'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
