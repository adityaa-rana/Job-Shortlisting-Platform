from fastapi import APIRouter,status,UploadFile,Depends,File
from src.resumes.dtos import resumeResponseSchema
from src.users.controller import get_current_user
from sqlalchemy.orm import Session
from src.utils.db import getdb
from src.resumes import controller

resume_routes=APIRouter(prefix="/resumes")

@resume_routes.post("/upload",response_model=resumeResponseSchema,status_code=status.HTTP_201_CREATED)
def upload_resume(file:UploadFile=File(...),current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.upload_resume(file,current_user,db)

@resume_routes.get("/getall",response_model=list[resumeResponseSchema],status_code=status.HTTP_200_OK)
def getall(current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.get_all_resumes(current_user,db)

@resume_routes.get("/get/{resume_id}",response_model=resumeResponseSchema,status_code=status.HTTP_200_OK)
def get(resume_id:int,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.get_resume(resume_id,current_user,db)

@resume_routes.delete("/delete/{resume_id}",status_code=status.HTTP_200_OK)
def delete_resume(resume_id:int,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.delete_resume(resume_id,current_user,db)

@resume_routes.get("/analyze/{resume_id}",response_model=resumeResponseSchema,status_code=status.HTTP_200_OK)
def analyze_resume(resume_id:int,current_user=Depends(get_current_user),db:Session=Depends(getdb)):
    return controller.analyze_resume(resume_id,current_user,db)