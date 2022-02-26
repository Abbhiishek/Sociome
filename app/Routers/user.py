from http.client import HTTPException
# import psycopg2
import time
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
from fastapi import  Response, status, HTTPException, Depends, APIRouter

# from sqlalchemy.sql.functions import func
from .. import  Schemas , models , oauth2
from .. database import get_db 
from . import hashing
router= APIRouter(prefix="/users",
    tags=['Users'])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Schemas.UserOut)
def User_SignUp(content:Schemas.UserCreate , db: Session = Depends(get_db)):
    new_user = models.User(**content.dict())
    hashed_password = hashing.hash(new_user.password)
    new_user.password= hashed_password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#to fetch a single user from the database
@router.get('/{username}', response_model=Schemas.UserOut)
def get_user(username: str, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with username: {username} does not exist")

    return user
