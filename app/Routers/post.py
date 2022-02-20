from csv import list_dialects
from http.client import HTTPException
# import psycopg2
import time
from typing import List, Optional
from sqlalchemy import desc, func
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
from fastapi import  Response, status, HTTPException, Depends, APIRouter

# from sqlalchemy.sql.functions import func
from .. import  Schemas , models ,oauth2
from .. database import get_db , Base
from .. models import Post

router= APIRouter(prefix="/posts",
    tags=['Posts'])


# This path OPERATION is to retrieve all the post from the data base @
@router.get("/",status_code=status.HTTP_200_OK , response_model=List[Schemas.PostOut]) #it get all the posts
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user) , limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # cur.execute("""SELECT * FROM posts  ORDER BY created_at DESC""")
    # posts=cur.fetchall()

    if not current_user:
         raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
        detail= f"You are not Logged in !, Try to Login with username & Password !")


    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.post_id, isouter=True).order_by(Post.created_at.desc()).group_by(models.Post.post_id).filter(models.Post.content.contains(search)).limit(limit).offset(skip).all()
    return posts

# This path OPERATION is to retrieve all the post of the logged in user !
@router.get("/logged_user",status_code=status.HTTP_200_OK , response_model=List[Schemas.PostOut]) #it get all the posts
def get_yours_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("""SELECT * FROM posts  ORDER BY created_at DESC""")
    # posts=cur.fetchall()

    if not current_user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
        detail= f"You are not Logged in !, Try to Login with username & Password !")

    posts=db.query(models.Post , func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.post_id, isouter=True).group_by(models.Post.post_id).filter(models.Post.author == current_user.username).order_by(Post.created_at.desc()).all()


    # posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
    #     models.Vote, models.Vote.post_id == models.Post.post_id, isouter=True).group_by(models.Post.post_id).filter(models.Post.post_id == id).first()

    if not posts:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail= f"You don't have any Post , Try to Create One !")


    return posts


#This path operation create a single post 
@router.post("/", status_code=status.HTTP_201_CREATED , response_model=Schemas.Post) 
def create_posts(content:Schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # we are passing the information that we need to pass from body as dictionary and store it in content 
    # cur.exectue(f"INSERT INTO posts (title, content, published) VALUES({post.title}, {post.content})")
    # cur.execute("""INSERT INTO posts (content, published ,image) VALUES (%s, %s , %s) RETURNING * """,(content.content, content.published,content.image))
    # created_post = cur.fetchone()
    # conn.commit()
    new_post = models.Post(author=current_user.username,**content.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


#This path operation is to find a single post already in the database by the post id :
@router.get("/{id}", status_code=status.HTTP_302_FOUND , response_model=Schemas.PostOut)
def get_post(id : int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute(""" SELECT * FROM posts WHERE post_id = %s """, (str(id),))
    # post=cur.fetchone()
    # post=db.query(models.Post).filter(models.Post.post_id==id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.post_id, isouter=True).group_by(models.Post.post_id).filter(models.Post.post_id == id).first()

    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
        detail= f"Post with an id of {id} is not Found .")
    return post

# This path operation is to delete a single post by its id 

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("""SELECT * FROM posts WHERE post_id = %s RETURNING * """, (str(id),))
    # post=cur.fetchone()
    post_query = db.query(models.Post).filter(models.Post.post_id == id)
    post = post_query.first()
    if  post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       detail=f"post with id: {id} was not found")

    if post.author != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
                       
    if  post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       detail=f"post with id: {id} was not found")
    # cur.execute("""DELETE FROM posts WHERE post_id = (%s) """,(id))
    # conn.commit()
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}" , status_code=status.HTTP_201_CREATED, response_model=Schemas.Post)
def update_post(id : int, content:Schemas.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute(""" UPDATE posts SET  content = %s , published = %s ,image =%s WHERE post_id = %s RETURNING * """,(content.content, content.published,content.image,str(id),))
    # post=cur.fetchone()
    post_query = db.query(models.Post).filter(models.Post.post_id == id)
    post = post_query.first()
    if post.author != current_user.username:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                       detail=f"post with id: {id} was not found")
    
    post_query.update(content.dict(),synchronize_session=False)
    db.commit()
    # conn.commit()
    return post_query.first()