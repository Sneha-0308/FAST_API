from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from .hasing import Hash
# from . import models
# dot represent importing schemas file from same directory


app = FastAPI()
models.Base.metadata.create_all(engine)  # this is related to creating table


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""here you can see that we have invoked request: schemas.Blog from schemas
 file so that title and attributes are used"""


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)  # this whole part is used to create table
    db.add(new_blog)                                                #
    db.commit()                                                     #
    db.refresh(new_blog)                                            #
    return new_blog                                                 #


# in delete we didn't used request because while deleting table schemas is not required


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()  # whenever you make change in db.query you have to commit the changes using db.commit() method
    return 'done'


# we require request:schemas.Blog because if you remove that you won't get parameter in put that is title and body
# db.query(models.Blog).filter(models.Blog.id == id).update({'title': 'updated title'}) this for only updating title
@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    blog.update({'title': request.title, 'body': request.body})
    db.commit()
    return 'updated successfully'


"""here we are using list because set of data is going to represent that's why we have used list"""


@app.get('/blog', response_model=List[schemas.showBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    # here we didnt used commit because we just seeing the content not modifying in content
    return blogs


@app.get('/blog/{id}', status_code=200, response_model=schemas.showBlog)  # default status code as 200
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')  # detail is keyword
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f'Blog with the id {id} is not available'}
    return blog




@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):

    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
