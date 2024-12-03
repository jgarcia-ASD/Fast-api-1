from typing import Optional
from fastapi import FastAPI
from app.models.UserModel import User
from app.crud import create_user, get_users

app = FastAPI()

@app.get("/pruebas")
def read_root():
    return {"Firts": " Hello World"}

@app.get("/pruebas/{item_id}")
def get_items(search: Optional[str] = None, skip: Optional[int] = 0, limit: Optional[int] = 10):
    return {"search": search, "skip": skip, "limit": limit}

@app.post("/users/")
def create_user(user: User):
    return {"name": user.name, "age": user.age, "email": user.email}

@app.post("/users/")
def create_user_endpoint(user: User):
    return create_user(user)

@app.get("/users/")
def get_users_endpoint():
    return get_users()