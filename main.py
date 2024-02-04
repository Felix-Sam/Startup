# main.py
from fastapi import FastAPI, HTTPException
from database import SessionLocal, engine
from crud import create_job, get_all_available_jobs, get_single_job, delete_job, update_job
from model import Base
from schemas import *

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# welcome endpoint
@app.get('/')
async def welcome():
    return f'Welcome to the API'

# posting of jobs
@app.post('/post_jobs')
async def create_job_endpoint(job: Postjob):
    db = SessionLocal()
    result = create_job(db, job)
    db.close()
    return result

# getting all available jobs
@app.get('/get_available_jobs')
async def get_all_available_jobs_endpoint():
    db = SessionLocal()
    result = get_all_available_jobs(db)
    db.close()
    return result

# get a job
@app.get('/single_job/{job_id}')
async def get_single_job_endpoint(job_id: int):
    db = SessionLocal()
    result = get_single_job(db, job_id)
    db.close()
    return result

# deleting a job
@app.delete('/delete_job')
async def delete_job_endpoint(id: int):
    db = SessionLocal()
    result = delete_job(db, id)
    db.close()
    return result

# update job status
@app.put('/jobs/{job_id}')
async def update_job_endpoint(job_id: int, job: Postjob):
    db = SessionLocal()
    result = update_job(db, job_id, job)
    db.close()
    return result
