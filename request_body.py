from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]  # value of this will be true because the default value of boolean is True


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f"Blog is created with title as {request.title}"}


# if __name__=="__main__":
#     uvicorn.run(app, host='127.0.0.1', port=9000)

""" Above statement is used to change the port number. after 
typing this in terminal you i have to just use command python request_body.py"""