# model.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PostJobModel(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True, index=True)
    job_title = Column(String, index=True)
    job_description = Column(String)
    job_location = Column(String)
    job_status = Column(String)
    job_duration = Column(String)
    job_image = Column(String)
    job_category = Column(String)
    author = Column(String)
    date_created = Column(DateTime, default=datetime.now)
    date_updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    promoted = Column(Boolean)
