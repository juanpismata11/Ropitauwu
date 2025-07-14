from fastapi import APIRouter
#from jwt_manager import create_token
from fastapi.responses import JSONResponse
from schema.user import User
from fastapi.encoders import jsonable_encoder
from config.database import Session
from services.user import UserService
from typing import List


user_router = APIRouter()

# Rutas para poder gets, posts y eso de users

@user_router.get('/users', response_model=List[User], status_code=200)
def get_users():
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.get('/users/{id}', response_model=User, status_code=200)
def get_user(id: int):
    db = Session()
    result = UserService(db).get_user_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "User not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.post('/users', response_model = dict, status_code=201)
def create_user(user : User):
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "User created successfully"})

@user_router.put('/users/{id}', response_model = dict, status_code = 200)
def update_user(id: int, user: User):
    db = Session()
    result = UserService(db).get_user_by_id(id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'User not found'})
    UserService(db).update_user(id, user)
    return JSONResponse(status_code=200, content={"message": "User updated successfully"})

@user_router.delete('/users/{id}', response_model = dict, status_code = 200)
def delete_user(id: int):
    db = Session()
    result = UserService(db).get_user_by_id(id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'User not found'})
    UserService(db).delete_user(id)
    return JSONResponse(status_code=200, content={"message": "User deleted successfully"})