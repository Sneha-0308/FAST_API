from fastapi import FastAPI

myapp = FastAPI()


@myapp.get('/')
def basic():
    return {"Greetings":"hey!!"}


@myapp.get('/about')
def about():
    return {"data":"About page"}