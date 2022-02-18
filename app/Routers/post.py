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

router= APIRouter(prefix="/posts",
    tags=['Posts'])


#commented out  as we are going to use the sqlalchemy instance to perform database operation

# while True:
#     try:
#         # Connect to an existing database
#         conn =psycopg2.connect(host='localhost', database='Sociome', user='postgres',password='abhishek1234',cursor_factory=RealDictCursor)

#         # Open a cursor to perform database operations
#         cur = conn.cursor()
#         print("Connection With Database is established !")
#         break
#     except Exception as error:
#         print ("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)

# This path OPERATION is to retrieve all the post from the data base @
@router.get("/",status_code=status.HTTP_200_OK) #it get all the posts
def get_posts(db: Session = Depends(get_db)):
    # cur.execute("""SELECT * FROM posts  ORDER BY created_at DESC""")
    # posts=cur.fetchall()
    posts=db.query(models.Post).all()
    return posts


#This path operation create a single post 
@router.post("/", status_code=status.HTTP_201_CREATED) 
def create_posts(content:Schemas.PostBase,db: Session = Depends(get_db)):
    # we are passing the information that we need to pass from body as dictionary and store it in content 
    # cur.exectue(f"INSERT INTO posts (title, content, published) VALUES({post.title}, {post.content})")
    # cur.execute("""INSERT INTO posts (content, published ,image) VALUES (%s, %s , %s) RETURNING * """,(content.content, content.published,content.image))
    # created_post = cur.fetchone()
    # conn.commit()
    new_post = models.Post(**content.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


#This path operation is to find a single post already in the database by the post id :
@router.get("/{id}", status_code=status.HTTP_302_FOUND)
def get_post(id : int, db: Session = Depends(get_db)):
    # cur.execute(""" SELECT * FROM posts WHERE post_id = %s """, (str(id),))
    # post=cur.fetchone()
    post=db.query(models.Post).filter(models.Post.post_id==id).first()

    if not post:

        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail= f"Post with an id of {id} is not Found .")
    return post

# This path operation is to delete a single post by its id 

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int,db: Session = Depends(get_db)):
    # cur.execute("""SELECT * FROM posts WHERE post_id = %s RETURNING * """, (str(id),))
    # post=cur.fetchone()
    post=db.query(models.Post).filter(models.Post.post_id==id).first()


    
    if  post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       details=f"post with id: {id} was not found")
    # cur.execute("""DELETE FROM posts WHERE post_id = (%s) """,(id))
    # conn.commit()
    post.delete(synchronize_session = False)
    db.commit()


    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}" , status_code=status.HTTP_201_CREATED)
def update_post(id : int, content:Schemas.PostBase,db: Session = Depends(get_db)):
    # cur.execute(""" UPDATE posts SET  content = %s , published = %s ,image =%s WHERE post_id = %s RETURNING * """,(content.content, content.published,content.image,str(id),))
    # post=cur.fetchone()

    post = db.query(models.Post).filter(models.Post.post_id==id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       details=f"post with id: {id} was not found")

    post.update(content.dict(),synchronize_session = False)
    db.commit()
    # conn.commit()



    return post