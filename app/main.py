import datetime
from distutils.log import error
from random import randrange
from fastapi.params import Body
from typing import Dict
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from . import developers , CustomMsg ,models
from .Routers import post , user ,auth , vote
from .database import engine 

# Alembic is gonna  make all the changes for the database  
# with --autogenerte tag of alembic 
# models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Sociome",
    description="Social Media Api",
    version= "V.1.00.02"
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://abbhishek.me"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# root operation 
@app.get("/")
def read_root():

    return {"Title":"SOCIOME" , "Description": "Social Media Api","Creator":"Code For Community", "Founded_By":"Abhishek Kushwaha" ,"Version":"1.0.0","Started_AT":"Janurary 2022"}
    

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
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(developers.router)
app.include_router(CustomMsg.router)
app.include_router(post.router)
app.include_router(vote.router)
