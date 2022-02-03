from fastapi.params import Body
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from typing import Optional


router= APIRouter(prefix="/CustomeMsg",
    tags=['Custome Msg Details'])

# This path operation is to send a custom messgae to the api and retrieve it (just for learning purpose !)
@router.get("/{author_id}/{msg}/{Author_Name}")
def read_item(author_id: int, msg: Optional[str] = None, Author_Name:Optional[str]= None):
    return {"Author_Id": author_id,"Author_Name": Author_Name, "Message": msg }

    '''    {
    "Author_Id": 1,
    "Author_Name": "abhishek kushwaha",
    "Message": "hello i am testing the api"
    }'''