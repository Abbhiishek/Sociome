from email.mime import image
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Post(Base):

    __tablename__= "posts"

    post_id = Column (Integer, primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    reacts = Column(Integer, nullable=False, server_default='0')
    image = Column(String)
    published = Column (Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))