from fastapi import FastAPI ,HTTPException,Depends,status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine ,sessionmaker
from sqlalchemy.orm import Session
app = FastAPI()

models.Base.metadata.create_all(bind = engine)

class PostBase(BaseModel):
    title: str
    content: str
    user_id:int

class UserBase(BaseModel):
    username: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency =Annotated[Session ,Depends(get_db)]

@app.delete("/posts/{post_id}",status_code = status.HTTP_200_OK)
async def delete_post(post_id: int,db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id ==post_id).first()
    if db_post is None:
        raise HTTPException(status_code =404,detail = "post was not found" )

    db.delete(db_post)
    db.commit()
                  

@app.post("/posts/",status_code = status.HTTP_201_CREATED)
async def create_post(post:PostBase ,db: db_dependency):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()

@app.post("/users/",status_code = status.HTTP_201_CREATED)
async def create_user(user:UserBase ,db: db_dependency):
    # db_user = models.User(**user.dict())
    new_post = Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post 

@app.get("/users/{user_id}", status_code = status.HTTP_201_CREATED)
async def read_user(user_id:int , db: db_dependency):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    if user is None:
        raise(HTTPException(status_code =404, details ="user is not found"))
    return user

