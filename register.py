from fastapi import FastAPI
# from pydantic import BaseModel

app = FastAPI()

signupdb = []


class Login():
    username: str
    password: str
    email: str
    phone: int


@app.get('/User')
def show():
    return {'details': signupdb}


@app.post('/User/{id}')
def add_user(request: Login):
    signupdb.append(request.dict())
    return signupdb[-1]


