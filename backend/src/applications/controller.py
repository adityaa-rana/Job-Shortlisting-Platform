from src.applications.models import applicationModel
from src.jobs.models import jobModel
from src.applications.dtos import updateApplicationSchema,applyJobSchema
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from src.resumes.models import resumeModel
from src.resumes.models import resumeModel
from src.roadmap_tasks.models import roadmapTaskModel
from src.ai.services import calculate_missing_skills
from src.ai.services import ( generate_learning_roadmap)
from src.roadmap_tasks.models import roadmapTaskModel
from src.ai.matcher import semantic_skill_matching
from src.ai.ats import calculate_ats_score

def apply_job(body:applyJobSchema,current_user,db:Session):
    if current_user.role!="candidate":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only candidates can apply")

    job=db.query(jobModel).filter(jobModel.id==body.job_id).first()

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found")

    resume=db.query(resumeModel).filter(resumeModel.id==body.resume_id).first()

    if not resume:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resume not found")

    if resume.candidate_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Access denied")

    if not resume.extracted_text:
         raise HTTPException(status_code=400,detail="Analyze resume first")
    
    if not job.jd_text:
         raise HTTPException(status_code=400,detail="Job description not analyzed")
    
    if not resume.extracted_skills:
        raise HTTPException(status_code=400,detail="Resume skills not extracted")

    if not job.jd_skills:
        raise HTTPException(status_code=400,detail="JD skills not extracted")
    

    resume_skills = resume.extracted_skills.split(",")

    jd_skills = job.jd_skills.split(",")
    
    matches = semantic_skill_matching(
        resume_skills,
        jd_skills
    )

    ats_score = calculate_ats_score(
        matches,
        len(jd_skills)
    )
    missing_skills = calculate_missing_skills(
        matches,
        jd_skills
    )
    learning_roadmap=generate_learning_roadmap(
        missing_skills
    )
    
    application=applicationModel(
        candidate_id=current_user.id,
        job_id=job.id,
        resume_id=resume.id,
        ats_score=ats_score,
        missing_skills=missing_skills,
        learning_roadmap=learning_roadmap
    )

    db.add(application)
    db.commit()
    db.refresh(application)
    tasks = []

    for line in learning_roadmap.split("\n"):

        line=line.strip()

        if ( line
            and not line.lower().startswith("week")
        ):

            tasks.append(line)

    for task in tasks:

        roadmap_task=roadmapTaskModel(

            application_id=application.id,

            task=task,

            completed=False
        )

        db.add(roadmap_task)

    db.commit()
    return application


# currently unused
def get_my_applications(current_user,db:Session):
    if current_user.role!="candidate":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only candidates can view their applications")
    applications=db.query(applicationModel).filter(applicationModel.candidate_id==current_user.id).all()
    return applications



def get_application(application_id:int,current_user,db:Session):

    if current_user.role!="candidate":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only candidates can view their applications")
    application=db.query(applicationModel).filter(applicationModel.id==application_id).first()
    if not application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Application not found")
    if application.candidate_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Unauthorized user")

    return application



def withdraw_application(application_id: int, current_user, db: Session):

    if current_user.role != "candidate":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only candidates can withdraw their applications"
        )

    application = db.query(applicationModel).filter(
        applicationModel.id == application_id
    ).first()

    if not application:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found"
        )

    if application.candidate_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Unauthorized user"
        )

    deleted = db.query(roadmapTaskModel).filter(
        roadmapTaskModel.application_id == application.id
    ).delete(synchronize_session=False)

    print("Deleted roadmap tasks:", deleted)

    db.commit()          # <-- Commit task deletion first

    db.delete(application)

    db.commit()

    return None



def update_application(application_id:int,body:updateApplicationSchema,current_user,db:Session):

    if current_user.role!="recruiter":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only recruiters can update applications")

    application=db.query(applicationModel).filter(applicationModel.id==application_id).first()

    if not application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Application not found")

    job=db.query(jobModel).filter(jobModel.id==application.job_id).first()

    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found")

    if job.recruiter_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Unauthorized user")

    updated_dict=body.model_dump(exclude_none=True)

    for key,value in updated_dict.items():
        setattr(application,key,value)

    db.commit()
    db.refresh(application)

    return application




def get_application_resume(application_id:int,current_user,db:Session):
    if current_user.role!="recruiter":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Only recruiters can view resumes")
    
    application=db.query(applicationModel).filter(applicationModel.id==application_id).first()

    if not application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Application not found")
    
    job=db.query(jobModel).filter(applicationModel.job_id==jobModel.id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Job not found")

    if job.recruiter_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Unauthorized")
    
    resume=db.query(resumeModel).filter(resumeModel.id==application.resume_id).first()
    if not resume:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resume not found")

    return resume


