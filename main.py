import datetime
from fastapi.params import Body
from typing import Optional
import time
from datetime import date, time,datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Title":"SOCIOME- Social Media Api","Creator":"Code For Community", "Founded_By":"Abhishek Kushwaha" ,"Version":"1.0.0","Started_AT":"Janurary 2022"}


@app.get("/developers")
def read_item():
    return {1:{"Name": "Abhishek Kushwaha", "Github_id": "https://github.com/Abbhiishek"},
    2:{"Name": "Amandeep Singh", "Github_id": "https://github.com/Aman8017k"},
    3:{"Name": "Shivam Basak", "Github_id": "https://github.com/shivamBasak"},
    4:{"Name": "Anjali Gupta", "Github_id": "https://github.com/anjalig18"},
    5:{"Name": "Anshita Choubey", "Github_id": "https://github.com/Anshitachoubey07"},
    6:{"Name": "Muskaan Purkait Alam", "Github_id": "https://github.com/Muskaanpurkait"},
    7:{"Name": "Priya Singh", "Github_id": "https://github.com/Priyasinghjis"},
    8:{"Name": "Roshimkana Pal", "Github_id": "https://github.com/Abbhiishek"},
    9:{"Name": "Koushik Das", "Github_id": "https://github.com/koushik-das123"},
    }

@app.get("/CustomeMsg/{author_id}/{msg}/{Author_Name}")
def read_item(author_id: int, msg: Optional[str] = None, Author_Name:Optional[str]= None):
    return {"Author_Id": author_id,"Author_Name": Author_Name, "Message": msg }

    '''    {
    "Author_Id": 1,
    "Author_Name": "abhishek kushwaha",
    "Message": "hello i am testing the api"
    }'''

@app.get("/time")
def read_item():
    time = datetime.today()
    isoTime= time.isoformat()
    return {"Today Date": isoTime}

@app.get("/posts") #it get all the posts
def get_posts():
    return{"Posts":{1:{"Name":"SOCIOME Posts 01"},
                    2:{"Name":"Amandeep"},
                    }}
@app.post("/create_posts") #it create a single post 
def create_posts(content:dict= Body(...)): # we are passing the information that we need to pass from body as dictionary and store it in content 
    return{"Status":"Posts Created !" , "Posts":content} # reteriving the body content , but its not being stored now !!!