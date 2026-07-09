from fastapi import APIRouter,status,Depends
from src.users.dtos import userRegisterSchema,userResponseSchema,loginResponseSchema,loginSchema,updateUserSchema
from src.users import controller
from src.utils.db import getdb
from sqlalchemy.orm import Session

user_routes=APIRouter(prefix="/users")

@user_routes.post("/register",response_model=userResponseSchema,status_code=status.HTTP_201_CREATED)
def register(body:userRegisterSchema,db:Session=Depends(getdb)):
    return controller.register_user(body,db)

@user_routes.post("/login",response_model=loginResponseSchema,status_code=status.HTTP_200_OK)
def login(body:loginSchema,db:Session=Depends(getdb)):
    return controller.login_user(body,db)

@user_routes.get("/getuser",response_model=userResponseSchema,status_code=status.HTTP_200_OK)
def get_user(current_user=Depends(controller.get_current_user),db:Session=Depends(getdb)):
    return current_user

@user_routes.put("/update",response_model=userResponseSchema,status_code=status.HTTP_200_OK)
def update_user(body:updateUserSchema,current_user=Depends(controller.get_current_user),db:Session=Depends(getdb)):
    return controller.update_user(body,current_user,db)

@user_routes.delete("/delete",status_code=status.HTTP_200_OK)
def delete_user(current_user=Depends(controller.get_current_user),db:Session=Depends(getdb)):
    return controller.delete_user(current_user,db)