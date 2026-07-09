from fastapi import APIRouter,status,Depends,UploadFile,Form,File
from src.jobs.dtos import jobResponseSchema,createJobSchema,updateJobSchema
from src.applications.dtos import applicationResponseSchema
from src.jobs import controller

from src.users.controller import get_current_user
from src.utils.db import getdb
from sqlalchemy.orm import Session
from typing import List

job_routes=APIRouter(prefix="/jobs")

# can't use createJobSchema because fastpi can't parse pydantic model and a file together
@job_routes.post("/create",response_model=jobResponseSchema,status_code=status.HTTP_201_CREATED)
def create_job(title:str=Form(...),
    description:str=Form(...),
    experience_level:str=Form(...),
    jd_file:UploadFile=File(...),
    current_user=Depends(get_current_user),
    db:Session=Depends(getdb)
):
    return controller.create_job(
        title,
        description,
        experience_level,
        jd_file,
        current_user,
        db
    )

@job_routes.get("/getall",response_model=List[jobResponseSchema],status_code=status.HTTP_200_OK)
def get_all_jobs(db:Session=Depends(getdb)):
    return controller.get_all_jobs(db)

@job_routes.get("/get_job/{job_id}",response_model=jobResponseSchema,status_code=status.HTTP_200_OK)
def get_job(job_id:int,db:Session=Depends(getdb)):
    return controller.get_job(job_id,db)

@job_routes.put("/update/{job_id}",response_model=jobResponseSchema,status_code=status.HTTP_200_OK)
def update_job(job_id:int,body:updateJobSchema,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.update_job(job_id,body,current_user,db)

@job_routes.delete("/delete/{job_id}",status_code=status.HTTP_200_OK)
def delete_job(job_id:int,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.delete_job(job_id,current_user,db)

@job_routes.get("/{job_id}/applications",response_model=list[applicationResponseSchema],status_code=status.HTTP_200_OK)
def get_job_applications(job_id:int,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.get_job_applications(job_id,current_user,db)

@job_routes.get("/top_candidates/{job_id}",response_model=list[applicationResponseSchema],status_code=status.HTTP_200_OK)
def get_top_candidates(job_id:int,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.get_top_candidates(job_id,current_user,db)

@job_routes.get("/my-jobs",response_model=list[jobResponseSchema])
def get_my_jobs_route(current_user = Depends(get_current_user),db: Session = Depends(getdb)):

    return controller.get_my_jobs(current_user,db)