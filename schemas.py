# schemas.py
from pydantic import BaseModel
from datetime import datetime

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
    date_updated: str
    date_created: str
