# Welcome 👋

CFCApi is a API DEVELOPMENT PROJECT UNDER CODE FOR COMMUNITY !


# Project Walkthrough 🚀

- CFCApi run on Python using FASTapi Framework [Docs](https://fastapi.tiangolo.com/)
- The project is under the Guidance of [Abhishek Kushwaha](https://twitter.com/abbhishek_k)


# Installation ☘️

- To install The Fastapi on the system

      pip install fastapi
- To install all the dependiencies at once use :

      pip install fastapi[all]
- Run the server in LocalHost:
  
      uvicorn main:app --reload
- Open your browser at !


      http://127.0.0.1:8000/
- Interactive API doc

      http://127.0.0.1:8000/docs 
# Sample code 🛠

```python
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
```

## 🙏 Support

-This project needs a ⭐️ from you. Don't forget to leave a star ⭐️

-Follow me [here](https://twitter.com/abbhishek_k) ✨

-Contributions to the project are most welcome! 😊

-Feel free to fork this repo and contribute. 🔧

-Thank You!👍
