from sqlalchemy.orm import Session

from src.jobs.models import jobModel

from src.interview_questions.services import generate_interview_questions

from fastapi import HTTPException,status


def get_interview_questions(
    job_id:int,
    db:Session
):

    job=db.query(
        jobModel
    ).filter(
        jobModel.id==job_id
    ).first()

    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )

    return {
        "questions":
        generate_interview_questions(
            job.jd_skills
        )
    }