from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db 
app=FastAPI()
fake_db = {}

@app.get('/')

def home():
    return{"welcome to todo list app"}


class todoapp(BaseModel):
    id:int
    title:str
    description:str
@ app.post("/id/")
def create_id(id:int):
    return{"result":id}

@ app.get("/title")
def read_title(title:str):
    return{"result":title}

@ app.get("/description")
def read_description(description:str):
    return{"result":description}


