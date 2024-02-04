# crud.py
from sqlalchemy.orm import Session
from model import PostJobModel
from schemas import Postjob
from datetime import datetime

def create_job(db: Session, job: Postjob):
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
    db.refresh(new_job)
    return new_job

def get_all_available_jobs(db: Session):
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

def get_single_job(db: Session, job_id: int):
    job = db.query(PostJobModel).filter(PostJobModel.id == job_id).first()
    if not job:
        return None
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
    return job_data

def delete_job(db: Session, job_id: int):
    job_to_delete = db.query(PostJobModel).filter_by(id=job_id).first()
    if job_to_delete:
        db.delete(job_to_delete)
        db.commit()
        return f'Job with {job_id} deleted successfully'
    else:
        return f'Job with such id does not exist'

def update_job(db: Session, job_id: int, job: Postjob):
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
        return None
    for key, value in job_data.items():
        setattr(existing_job, key, value)
    db.commit()
    return existing_job
