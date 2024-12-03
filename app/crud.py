# crud.py

from typing import List
from app.models.UserModel import User

# Simulación de una base de datos en memoria
fake_users_db = []

def create_user(user: User):
    fake_users_db.append(user)
    return user

def get_users() -> List[User]:
    return fake_users_db
