from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from blog import models, schemas
from blog.database import engine, SessionLocal

# from . import models
# dot represent importing schemas file from same directory


app = FastAPI()
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()  # whenever you make change in db.query you have to commit the changes using db.commit() method
    return 'done'


# we require request:schemas.Blog because if you remove that you won't get parameter in put that is title and body
    # db.query(models.Blog).filter(models.Blog.id == id).update({'title': 'updated title'}) this for only updating title
@app.put('/blog/{id}', status_code=200)
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found')
    blog.update({'title': request.title, 'body': request.body}) #HERE 
    db.commit()
    return 'updated successfully'



@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=200)  # default status code as 200
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')  # detail is keyword
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f'Blog with the id {id} is not available'}
    return blog
