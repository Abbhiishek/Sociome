from sqlalchemy import Column,Integer, String, Boolean,ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP 
from .database import Base

# This is the structure of Post table in the database 
class Post(Base):

    __tablename__= "posts"

    post_id = Column (Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    reacts = Column(Integer, nullable=False, server_default='0')
    image = Column(String)
    published = Column (Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    author = Column(Integer , ForeignKey("users.user_id",ondelete="CASCADE"), nullable=False)
    author_details = relationship("User")
    

# This is the structure of user table in the database 
class User(Base):

    __tablename__= "users"
    user_id = Column (Integer, primary_key=True, nullable=False)
    email = Column (String , nullable=False, unique=True)
    password = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    fullname = Column(String)
    profile_pic = Column(String)
    bio = Column(String)
    github_link = Column(String)
    joined_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))