# Welcome 👋

Sociome is a API DEVELOPMENT PROJECT UNDER [CODE FOR COMMUNITY !](https://github.com/Abbhiishek/Code-For-Community) capable of CRUD operation and this api is specific with Social Media Application Functionalities.

[![Python application](https://github.com/Abbhiishek/Sociome/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/Abbhiishek/Sociome/actions/workflows/python-app.yml) 
[ ![View Project](https://img.shields.io/badge/view__Project-Deployed-blue)](https://abbhishek.me/Sociome/)
[ ![View Project](https://img.shields.io/github/issues/Abbhiishek/Sociome)](https://abbhishek.me/Sociome/)
[ ![View Project](https://img.shields.io/github/forks/Abbhiishek/Sociome)](https://abbhishek.me/Sociome/)
[ ![View Project](https://img.shields.io/github/stars/Abbhiishek/Sociome)](https://abbhishek.me/Sociome/)
[ ![View Project](https://img.shields.io/github/license/Abbhiishek/Sociome)](https://abbhishek.me/Sociome/)

# Tech-Stacks Used 🔮
  <p align="left"> 
   <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>
  <a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer"> <img src="https://fastapi.tiangolo.com/img/icon-white.svg" alt="FastApi" width="40" height="40"/> </a> 
  <a href="https://www.sqlalchemy.org/" target="_blank" rel="noreferrer"> <img src="https://www.sqlalchemy.org/img/sqla_logo.png" alt="sqlalchemy" width="100" height="40"/> </a>
  <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> 
  <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> 
  <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> 
   <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> 
   <a href="https://heroku.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/> </a> 
   </p>

# Project Walkthrough 🚀

- Sociome run on Python using FASTapi Framework [Docs](https://fastapi.tiangolo.com/)
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
