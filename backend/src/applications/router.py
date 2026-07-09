from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.applications import controller
from src.applications.dtos import applyJobSchema,applicationResponseSchema,updateApplicationSchema
from src.users.controller import get_current_user
from src.utils.db import getdb
from src.resumes.dtos import resumeResponseSchema

application_routes=APIRouter(prefix="/applications")

@application_routes.post("/apply",response_model=applicationResponseSchema,status_code=status.HTTP_201_CREATED)
def apply_job(body:applyJobSchema,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.apply_job(body,current_user,db)

@application_routes.get("/my-applications",response_model=list[applicationResponseSchema],status_code=status.HTTP_200_OK)
def get_my_applications(current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.get_my_applications(current_user,db)

@application_routes.get("/{application_id}",response_model=applicationResponseSchema,status_code=status.HTTP_200_OK)
def get_application(application_id:int,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.get_application(application_id,current_user,db)

@application_routes.put("/{application_id}",response_model=applicationResponseSchema,status_code=status.HTTP_200_OK)
def update_application(application_id:int,body:updateApplicationSchema,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.update_application(application_id,body,current_user,db)

@application_routes.delete("/delete/{application_id}",status_code=status.HTTP_200_OK)
def withdraw_application(application_id:int,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.withdraw_application(application_id,current_user,db)


@application_routes.get("/{application_id}/resume",response_model=resumeResponseSchema,status_code=status.HTTP_200_OK)
def get_application_resume(application_id:int,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.get_application_resume(application_id,current_user,db)


