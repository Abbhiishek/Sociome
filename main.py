import datetime
from typing import Optional
import time
from datetime import date, time,datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Messgaes": "Hey viewer ! i made it man !","Author":"Abhishek Kushwaha"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/author/{author_id}/{q}")
def read_item(author_id: int, q: Optional[str] = None):
    return {"item_id": author_id, "request": q ,"name":"Abhishek kushwaha"}

@app.get("/time")
def read_item():
    time = datetime.today()
    isoTime= time.isoformat()
    return {"Today Date": isoTime}

