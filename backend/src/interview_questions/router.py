from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.utils.db import getdb

from src.interview_questions import controller

question_routes=APIRouter(
    prefix="/questions"
)

@question_routes.get("/{job_id}")
def get_questions(
    job_id:int,
    db:Session=Depends(getdb)
):

    return controller.get_interview_questions(
        job_id,
        db
    )