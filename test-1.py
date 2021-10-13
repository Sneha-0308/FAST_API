from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# from typing import Optional

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    userid: str
    phone: str


users = []
userids = []


def doesuserexist(user: str):
    for x in range(len(users)):
        if users[x] == user:
            return True
        else:
            return False


@app.post('/login')
def login(user: User):
    res = {"response": "error"}
    for x in range(len(users)):
        if users[x] == user.name:
            if userids[x] == user.userid:
                res = {"response": "success"}
            else:
                res = {"response": "Incorrect userid"}
        else:
            res = {"response": "Incorrect name"}
    return res


@app.post('/register')
def register(user: User):
    res = {"response": "error"}
    if not(doesuserexist(user.name)):
        users.append(user.name)
        userids.append(user.userid)
        res = {"response": "success"}
    else:
        res = {"response": "user already exists"}
    return res