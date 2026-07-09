from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,Optional
from datetime import datetime

class userRegisterSchema(BaseModel):
    name:Annotated[str,Field(title="Name of the user")]
    email:Annotated[EmailStr,Field(title="Email of the user")]
    password:Annotated[str,Field(title="Password of the user",min_length=8  )]
    role:Annotated[str,Field(title="Role of the user")]

class userResponseSchema(BaseModel):
    model_config = {"from_attributes": True}
    id:Annotated[int,Field(title="Id of the user")]
    name:Annotated[str,Field(title="Name of the user")]
    email:Annotated[EmailStr,Field(title="Email of the user")]
    role:Annotated[str,Field(title="Role of the user")]
    created_at:Annotated[datetime,Field(title="Account creation time")]


class loginSchema(BaseModel):
    email:Annotated[EmailStr,Field(title="Email of the user")]
    password:Annotated[str,Field(title="Password of the user",min_length=8)]


class loginResponseSchema(BaseModel):
    access_token:Annotated[str,Field(title="JWT access token")]
    token_type:Annotated[str,Field(title="Token type")]
    

class updateUserSchema(BaseModel):
    name:Annotated[Optional[str],Field(title="Updated name of the user",default=None)]
    email:Annotated[Optional[EmailStr],Field(title="Email of the user",default=None)]
    password:Annotated[Optional[str],Field(title="Password of the user",default=None,min_length=8)]


# sqlalchemy using dtos expect dictionary 
# apart from userResponseSchema , all other models are receiving dictionary , but it receives pydantic object 
# model_config = {"from_attributes": True} , hence this line says read from object instead of dictionary