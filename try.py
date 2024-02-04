from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy.orm

SQLALCHEMY_DATABASE_URL = 'sqlite:///./PostJob.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()

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


Base.metadata.create_all(bind=engine)

app = FastAPI()
db = SessionLocal()

class Postjob(BaseModel):
    title: str
    description: str
    location: str
    job_status: str
    job_duration: str
    image: str
    job_category: str
    author: str
    promoted: bool
    date_updated:str
    date_created:str

# welcome endpoint
@app.get('/')
async def welcome():
    return f'Welcome to the API'

# posting of jobs
@app.post('/post_jobs')
async def create_job(job: Postjob):
    job_data = {
        "job_title": job.title,
        "job_description": job.description,
        "job_status": job.job_status,
        "job_duration": job.job_duration,
        "job_category": job.job_category,
        "date_created": datetime.now(),
        "job_image": job.image,
        "promoted": job.promoted,
        "author": job.author,
    }
    new_job = PostJobModel(**job_data)
    db.add(new_job)
    db.commit()
    db.close()
    return job_data

# getting all available jobs
@app.get('/get_available_jobs')
async def get_all_available_jobs():
    all_jobs = db.query(PostJobModel).all()
    available_jobs = []

    for job in all_jobs:
        job_data = {
            'job_id': job.id,
            "job_title": job.job_title,
            "job_description": job.job_description,
            "job_status": job.job_status,
            "job_duration": job.job_duration,
            "job_category": job.job_category,
            "date_created": job.date_created,
            "date_updated": job.date_updated,
            "job_image": job.job_image,
            "promoted": job.promoted,
            "author": job.author,
        }
        available_jobs.append(job_data)
    return available_jobs

# get a job
@app.get('/single_job/{job_id}')
def get_single_job(job_id: int):
    job = db.query(PostJobModel).filter(PostJobModel.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    job_data = {
        "job_id": job.id,
        "job_title": job.job_title,
        "job_description": job.job_description,
        "job_status": job.job_status,
        "job_duration": job.job_duration,
        "job_category": job.job_category,
        "date_created": job.date_created,
        "date_updated": job.date_updated,
        "job_image": job.job_image,
        "promoted": job.promoted,
        "author": job.author,
    }
    db.close()
    return job_data

# deleting a job
@app.delete('/delete_job')
async def delete_job(id: int):
    job_to_delete = db.query(PostJobModel).filter_by(id=id).first()
    if job_to_delete:
        db.delete(job_to_delete)
        db.commit()
        return f'Job with {id} deleted successfully'
    else:
        return f'Job with such id does not exist'

# update job status
@app.put('/jobs/{job_id}')
async def update_job(job_id: int, job: Postjob):
    job_data = {
        "job_title": job.title,
        "job_description": job.description,
        "job_status": job.job_status,
        "job_duration": job.job_duration,
        "job_category": job.job_category,
        "date_updated": datetime.now(),
        "job_image": job.image,
        "promoted": job.promoted,
        "author": job.author,
    }

    existing_job = db.query(PostJobModel).filter(PostJobModel.id == job_id).first()
    if not existing_job:
        raise HTTPException(status_code=404, detail="Job not found")
    for key, value in job_data.items():
        setattr(existing_job, key, value)
    db.commit()
    db.close()
    return job_data
