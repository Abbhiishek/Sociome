from http.client import HTTPException
# import psycopg2
import time
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
from fastapi import  Response, status, HTTPException, Depends, APIRouter

# from sqlalchemy.sql.functions import func
from .. import  Schemas , models
from .. database import get_db , Base
from .. models import Post

router= APIRouter(prefix="/users",
    tags=['Users'])


