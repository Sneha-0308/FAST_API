"""in this schemas file we will have our basemodel and it can be extended to anyother files
for example if you want to extend basemodel to main.py file first you have to import and then invoke schemas.Blog
here this Blog refer to basemodel"""

from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


"""this below class is used when you want to show the details of both
 value present in Blog class so we extend that class"""
# class showBlog(Blog):
#     class Config():
#         orm_mode = True

"""If you want to change the representation of dteails different form Blog class so you have to extend
 BaseModel and in that class you have to mention the argument which you wanted to reprent"""


class showBlog(BaseModel):
    title: str

    class Config():
        orm_mode = True


"""orm is used because we have used db.query which is belongs to sqlalchemy.orm"""


class User(BaseModel):
    name:str
    email:str
    password:str