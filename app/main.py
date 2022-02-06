import datetime
from distutils.log import error
from http.client import HTTPException
from random import randrange
from sqlite3 import DatabaseError
from urllib import response
from fastapi.params import Body
from typing import Optional
import time
from datetime import date, time,datetime
from fastapi import FastAPI,status
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import developers , CustomMsg , Schemas
 
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

# This path OPERATION is to retrieve all the post from the data base @
@app.get("/posts") #it get all the posts
def get_posts():
    cur.execute("""SELECT * FROM posts """)
    posts=cur.fetchall()
    return{"Posts":posts}


#This path operation create a single post 
@app.post("/create_posts", status_code=status.HTTP_201_CREATED) 
def create_posts(content:Schemas.PostBase):
    # we are passing the information that we need to pass from body as dictionary and store it in content 
    # cur.exectue(f"INSERT INTO posts (title, content, published) VALUES({post.title}, {post.content})")
    cur.execute("""INSERT INTO posts (content, published) VALUES (%s, %s) RETURNING * """,(content.content, content.published))
    created_post = cur.fetchone()
    conn.commit()
    return {"Created post ": created_post}


#This path operation is to find a single post already in the database by the post id :
@app.get("/posts/{id}", status_code=status.HTTP_302_FOUND)
def get_post(id : int):
    print(id)
    id=str(id)
    cur.execute("""SELECT * FROM posts WHERE post_id =(%s)""",(id))
    post=cur.fetchone()
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Status": "Post with an id of "+ id +" is not Found ."}
    return {"Status": "The post Id that you have choosen to retrieve is "+id,"ASKED Post":post}

# This path operation is to delete a single post by its id 

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    print(id)
    id=str(id)
    cur.execute("""SELECT * FROM posts WHERE post_id =(%s)""",(id))
    post=cur.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       details=f"post with id: {id} was not found")
    cur.execute("""DELETE FROM posts WHERE post_id = (%s) """,(id))
    conn.commit()
    return {"Status": "The post Id that you have choosen to delete is "+id,"Deleted Post":post}
















#including the routers from app pacakage !!!
app.include_router(developers.router)
app.include_router(CustomMsg.router)