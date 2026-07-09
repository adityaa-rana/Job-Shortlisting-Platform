from src.jobs.models import jobModel
from src.jobs.dtos import createJobSchema,updateJobSchema
from fastapi import HTTPException,status,UploadFile
from sqlalchemy.orm import Session
import os
from src.ai.parser import extract_text_from_pdf
from src.ai.preprocessing import clean_text
from src.ai.extractor import extract_skills
from src.ai.normalizer import normalize_skills

from src.applications.models import applicationModel

# recruiter creates a new job with jd upload
def create_job(title:str,description:str, experience_level:str,jd_file:UploadFile,current_user,db:Session):

    if current_user.role!="recruiter":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only recruiters can post jobs")

    upload_dir="uploads/jobs"

    # make directory if doesn;t exist
    os.makedirs(upload_dir,exist_ok=True)

    file_path=f"{upload_dir}/{jd_file.filename}"

    # save the jd in the folder
    with open(file_path,"wb") as f:
        f.write(jd_file.file.read())

    text = extract_text_from_pdf(file_path)

    text = clean_text(text)
    skills=extract_skills(text)
    normalized_skills = normalize_skills(skills)


    jd_skills=", ".join(normalized_skills)

    new_job=jobModel(
        title=title,
        description=description,
        experience_level=experience_level,
        recruiter_id=current_user.id,
        job_file_path=file_path,
        jd_text=text,
        jd_skills=jd_skills
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


# used by candidate
def get_all_jobs(db:Session):
    jobs=db.query(jobModel).all()

    # if not jobs:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No jobs found")

    return jobs


def get_job(job_id:int,db:Session):
    job=db.query(jobModel).filter(jobModel.id==job_id).first()

    # if not job:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found")

    return job

def get_my_jobs(current_user, db: Session):

    jobs = db.query(jobModel).filter(
        jobModel.recruiter_id == current_user.id
    ).all()

    # if not jobs:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail="No jobs found"
    #     )

    return jobs

def update_job(job_id:int,body:updateJobSchema,current_user,db:Session):
    job=db.query(jobModel).filter(jobModel.id==job_id).first()

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found")

    if current_user.id!=job.recruiter_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Unauthorized")

    updated_job_dict=body.model_dump(exclude_none=True)

    for key,value in updated_job_dict.items():
        setattr(job,key,value)

    db.commit()
    db.refresh(job)

    return job



def delete_job(job_id:int,current_user,db:Session):
    job=db.query(jobModel).filter(jobModel.id==job_id).first()

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found")

    if current_user.id!=job.recruiter_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Forbidden")

    db.delete(job)
    db.commit()

    return None


# by recruiter : get all applications for a particular job id
def get_job_applications(job_id:int,current_user,db:Session):
    if current_user.role!="recruiter":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only recruiter can see applications")
    
    job=db.query(jobModel).filter(jobModel.id==job_id).first()

    # check if job exists
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found")

    # check 
    if job.recruiter_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Unauthorized")
    
    applications=db.query(applicationModel).filter(applicationModel.job_id==job_id).order_by(applicationModel.ats_score.desc()).all()
    
    return applications

def get_top_candidates(job_id:int,current_user,db:Session):
    if current_user.role!="recruiter":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only recruiters can view candidates")
    
    job=db.query(jobModel).filter(jobModel.id==job_id).first()

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found")

    if job.recruiter_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Unauthorized")
    
    applicants=db.query(applicationModel).filter(applicationModel.job_id==job_id).order_by(applicationModel.ats_score.desc()).all()
    
    return applicants
