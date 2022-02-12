import datetime
from distutils.log import error
from http.client import HTTPException
from random import randrange
from sqlite3 import DatabaseError
from urllib import response
from fastapi.params import Body
from typing import Dict, Optional
import time
from datetime import date, time,datetime
from fastapi import FastAPI,status
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor
import time
from . import developers , CustomMsg , Schemas
from .Routers import post
app = FastAPI(
    title="Sociome",
    description="Social Media Api"
)

# root operation 
@app.get("/")
def read_root():
    return {"Title":"SOCIOME- Social Media Api","Creator":"Code For Community", "Founded_By":"Abhishek Kushwaha" ,"Version":"1.0.0","Started_AT":"Janurary 2022"}

# This operation delivers the current iso formatted time of the post requests !
@app.get("/time")
def read_item():
    time = datetime.today()
    isoTime= time.isoformat()
    return {"Today Date": isoTime}


@app.post("/trial")
def create(payload : Dict =Body(...)):
    print(payload)
    return{"Messgae": f"title : {payload['title']}  , content :{payload['message']}"}



#including the routers from app pacakage !!!
app.include_router(developers.router)
app.include_router(CustomMsg.router)
app.include_router(post.router)