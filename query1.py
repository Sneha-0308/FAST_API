from fastapi import FastAPI

app = FastAPI()



""" If you didn't mentioned the value we have to consider 
default so for that  """


@app.get('/blog')
# def index(limit, published: bool = True):
def index(limit, published: bool):
    """If you didn't mention the type of published then always
       condition will be true because that will be considered default
       as String datatype you can check that first you have to run this
       API without mentioning bool and uncomment the below return statement
       and also try the same with mentioning the bool (http://127.0.0.1:8000/blog?limit=10&published=false) """

    # return published

    if published:
        return {'data': f'{limit} published blogs from the DB'}
    else:
        return {'data': 'all published db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blog'}


""" If you didn't mentioned the value we have to consider 
default so for that  """
