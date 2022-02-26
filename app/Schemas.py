from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

# This is the main model of post that user will pass 
class PostBase(BaseModel):
    content: str #the main content of the post 
    published: bool =True #the post will be published or not default is set to true
    image: Optional[str]

    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass

# this is a response model for fetching user details or for creating the user
class UserOut(BaseModel):
    user_id: int
    fullname: str
    username: str
    bio: str
    profile_pic: str
    github_link: str
    email: EmailStr
    joined_at: datetime

    class Config:
        orm_mode = True





class Post(PostBase):
    post_id: int
    created_at: datetime
    author: str
    # owner: UserOut
    author_details: UserOut

    class Config:
        orm_mode = True

# this is a response model 
class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    fullname: Optional[str]
    username: str
    bio:Optional[str]
    profile_pic: Optional[str]
    github_link: Optional[str]

# this is a schemas model for updating user details
class UserUpdate(BaseModel):
    email: EmailStr
    password: str
    username : str
    bio:Optional[str]
    profile_pic: Optional[str]

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# the is the response schemas for token 
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)