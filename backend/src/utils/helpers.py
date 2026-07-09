from pwdlib import PasswordHash
from src.utils.settings import settings
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

password_hash = PasswordHash.recommended()
security = HTTPBearer()

def get_password_hash(password:str):
    return password_hash.hash(password)

def verify_password(plain_password:str, hash_password:str):
    return password_hash.verify(plain_password, hash_password)

def create_access_token(data:dict):
    expire_time = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_TIME)

    # id and email
    payload = data.copy()

    # id,email,exp
    payload.update({"exp": expire_time})

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return token

def verify_access_token(credentials:HTTPAuthorizationCredentials=Depends(security)):
    try:
        token = credentials.credentials

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        return payload

    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired, Login again")