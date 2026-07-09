from src.users.dtos import userRegisterSchema,userResponseSchema,updateUserSchema,loginResponseSchema,loginSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Depends
from src.users.models import UserModel
from src.utils.helpers import get_password_hash,verify_password,create_access_token,verify_access_token
from src.utils.db import getdb

# Session is a datatype : db is an object of LocalSession() of type Session
def register_user(body:userRegisterSchema,db:Session):
    is_user=db.query(UserModel).filter(UserModel.email==body.email).first()

    if is_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="User email already exists")

    hashed_password=get_password_hash(body.password)

    new_user=UserModel(
        name=body.name,
        email=body.email,
        hash_password=hashed_password,
        role=body.role.lower()
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(body:loginSchema,db:Session):
    user=db.query(UserModel).filter(UserModel.email==body.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")

    if not verify_password(body.password,user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid credentials")

    payload={"_id":user.id,"role":user.role}

    token=create_access_token(payload)

    return {"access_token":token,"token_type":"Bearer"}

def get_current_user(db:Session=Depends(getdb),payload:dict=Depends(verify_access_token)):
    user_id=payload.get("_id")

    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")

    user=db.query(UserModel).filter(UserModel.id==user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User not found")

    return user

def update_user(body:updateUserSchema,current_user,db:Session):
    updated_dict=body.model_dump(exclude_none=True)

    for key, value in updated_dict.items():

        if key == "password":
            current_user.hash_password = get_password_hash(value)
        else:
            setattr(current_user, key, value)

    db.commit()
    db.refresh(current_user)

    return current_user

def delete_user(current_user,db:Session):
    db.delete(current_user)
    db.commit()

    return None