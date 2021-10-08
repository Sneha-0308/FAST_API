from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"Data": "Blog list"}


"""# this runs fine"""


@app.get('/Blog/unpublished')
def unpublished():
    return {'data':'unpublished'}


@app.get('/Blog/{id}')
def blog(id: int):
    return {'data': id}


"""Throws the error """
# @app.get('/Blog/unpublished')
# def unpublished():
#     return {'data':unpublished}


@app.get('/Blog/{id}/{comment}')
def comn(id: int, comment: str):
    return {'data':{id, comment}}

"""Throws the error """
# @app.get('/Blog/unpublished')
# def unpublished():
#     return {'data':unpublished}