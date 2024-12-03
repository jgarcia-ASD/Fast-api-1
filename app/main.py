from typing import Optional
from fastapi import FastAPI

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