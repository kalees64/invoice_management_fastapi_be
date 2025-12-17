from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from fastapi import HTTPException, Depends, Cookie
from dotenv import load_dotenv
import os
from pydantic import EmailStr
from starlette import status
from typing import Annotated
from datetime import timedelta,datetime
from jose import jwt,JWTError

load_dotenv()

bearer_auth = HTTPBearer()

jwt_algorithm = os.getenv("JWT_ALGORITHM") or "HS256"
SECRET_ACCESS_KEY = os.getenv("SECRET_ACCESS_KEY") or "secret"

def verify_bearer_token(bearer_token:Annotated[HTTPAuthorizationCredentials,Depends(bearer_auth)]):
    if bearer_token.scheme == "Bearer" and bearer_token.credentials == SECRET_ACCESS_KEY:
        return {"token":bearer_token.credentials }
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Bearer Token")

def create_jwt_token(user:EmailStr,expires_delta:timedelta):
    expires = datetime.now()+expires_delta
    encode = {'sub':user,"exp":expires.timestamp()}
    return jwt.encode(encode,SECRET_ACCESS_KEY,jwt_algorithm)

def verify_jwt_token(bearer_jwt_token:Annotated[str,Depends(bearer_auth)]):
    try:
        if not bearer_jwt_token.scheme == "Bearer" or not bearer_jwt_token.credentials:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Bearer Token")
        jwt_token = bearer_jwt_token.credentials
        payload = jwt.decode(jwt_token,SECRET_ACCESS_KEY,algorithms=[jwt_algorithm])
        user:EmailStr=payload.get('sub')
        if user is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid JWT Token")
        return {"user":user}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid JWT Token")



def verify_jwt_cookie(access_token: str = Cookie(None)):
    try:
        if access_token is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Missing authentication cookie"
            )

        payload = jwt.decode(
            access_token,
            SECRET_ACCESS_KEY,
            algorithms=[jwt_algorithm]
        )

        user = payload.get("sub")
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid JWT Token"
            )

        return {"user": user}

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid JWT Token"
        )
