import datetime
from distutils.log import error
from random import randrange
from sqlite3 import DatabaseError
from fastapi.params import Body
from typing import Optional
import time
from datetime import date, time,datetime
from fastapi import FastAPI,status
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import developers
 
app = FastAPI()
while True:
    try:
        # Connect to an existing database
        conn =psycopg2.connect(host='localhost', database='Sociome', user='postgres',password='abhishek1234',cursor_factory=RealDictCursor)

        # Open a cursor to perform database operations
        cur = conn.cursor()
        print("Connection With Database is established !")
        break
    except Exception as error:
        print ("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)


#Schema 
class Post(BaseModel):
    post_id: Optional[int]   #will generate a random number as post_id (only for testing)
    content: str #the main content of the post 
    published: bool =True #the post will be published or not default is set to true 
    reacts: int = 0 # its the likes that the post have 
    created_at: str = datetime.now() # its the time at which the post was created 
#fake post dictionary

post=[{}]

# root operation 
@app.get("/")
def read_root():
    return {"Title":"SOCIOME- Social Media Api","Creator":"Code For Community", "Founded_By":"Abhishek Kushwaha" ,"Version":"1.0.0","Started_AT":"Janurary 2022"}



# This path operation is to send a custom messgae to the api and retrieve it (just for learning purpose !)
@app.get("/CustomeMsg/{author_id}/{msg}/{Author_Name}")
def read_item(author_id: int, msg: Optional[str] = None, Author_Name:Optional[str]= None):
    return {"Author_Id": author_id,"Author_Name": Author_Name, "Message": msg }

    '''    {
    "Author_Id": 1,
    "Author_Name": "abhishek kushwaha",
    "Message": "hello i am testing the api"
    }'''

# This operation delivers the current iso formatted time of the post requests !
@app.get("/time")
def read_item():
    time = datetime.today()
    isoTime= time.isoformat()
    return {"Today Date": isoTime}

# This path OPERATION is to retrieve all the post from the data base @
@app.get("/posts") #it get all the posts
def get_posts():
    cur.execute("""SELECT * FROM posts """)
    posts=cur.fetchall()
    print(posts)
    return{"Posts":posts}


#This path operation create a single post 
@app.post("/create_posts", status_code=status.HTTP_201_CREATED) 
def create_posts(content:Post):
    # we are passing the information that we need to pass from body as dictionary and store it in content 
    # cur.exectue(f"INSERT INTO posts (title, content, published) VALUES({post.title}, {post.content})")
    cur.execute("""INSERT INTO posts (content, published) VALUES (%s, %s) RETURNING * """,(content.content, content.published))
    created_post = cur.fetchone()
    conn.commit()
    return {"Created post ": created_post}
















#including the routers from app pacakage !!!
app.include_router(developers.router)