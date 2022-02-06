from distutils.log import error
from http.client import HTTPException
from random import randrange
from urllib import response
from fastapi.params import Body
from typing import Optional
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from fastapi.params import Body
from pydantic import BaseModel
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional
# from sqlalchemy.sql.functions import func
from .. import  Schemas


router= APIRouter(prefix="/posts",
    tags=['Posts'])

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

# This path OPERATION is to retrieve all the post from the data base @
@router.get("/") #it get all the posts
def get_posts():
    cur.execute("""SELECT * FROM posts """)
    posts=cur.fetchall()
    return{"Posts":posts}


#This path operation create a single post 
@router.post("/posts", status_code=status.HTTP_201_CREATED) 
def create_posts(content:Schemas.PostBase):
    # we are passing the information that we need to pass from body as dictionary and store it in content 
    # cur.exectue(f"INSERT INTO posts (title, content, published) VALUES({post.title}, {post.content})")
    cur.execute("""INSERT INTO posts (content, published ,image) VALUES (%s, %s , %s) RETURNING * """,(content.content, content.published,content.image))
    created_post = cur.fetchone()
    conn.commit()
    return {"Created post ": created_post}


#This path operation is to find a single post already in the database by the post id :
@router.get("/{id}", status_code=status.HTTP_302_FOUND)
def get_post(id : int):
    cur.execute(""" SELECT * FROM posts WHERE post_id = %s """, (str(id),))
    post=cur.fetchone()
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Status": "Post with an id of "+ id +" is not Found ."}
    return {"Status": "The post Id that you have choosen to retrieve is "+str(id),"ASKED Post":post}

# This path operation is to delete a single post by its id 

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    cur.execute("""SELECT * FROM posts WHERE post_id = %s RETURNING * """, (str(id),))
    post=cur.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       details=f"post with id: {id} was not found")
    cur.execute("""DELETE FROM posts WHERE post_id = (%s) """,(id))
    conn.commit()
    return {"Status": "The post Id that you have choosen to delete is "+str(id),"Deleted Post":post}



@router.put("/{id}" , status_code=status.HTTP_201_CREATED)
def update_post(id : int, content:Schemas.PostBase):
    cur.execute(""" UPDATE posts SET  content = %s , published = %s ,image =%s WHERE post_id = %s RETURNING * """,(content.content, content.published,content.image,str(id),))
    post=cur.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       details=f"post with id: {id} was not found")
    conn.commit()
    return {"Status": "The post Id with  {id} was deletd succesfully ","Deleted Post":post}