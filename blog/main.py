from fastapi import FastAPI
from . import schemas, models
from .database import engine
# from . import models
# dot represent importing schemas file from same directory


app = FastAPI()
models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: schemas.Blog):
    return request
