from fastapi import FastAPI

app=FastAPI()


@app.get('/')
def index():
    return {'Greeting': "Hello Welocme"}


@app.get('/blog')
def blog(limit):
    return {'data': f'{limit} blogs from the DB'}


"""In the API after /blog if you type /blog?limit=10 
then it gives the output as 10 blogs from the DB like this 
(http://127.0.0.1:8000/blog?limit=10)"""