from fastapi import APIRouter
from jwt_manager import create_token
from fastapi.responses import JSONResponse
from models.user import User


user_router = APIRouter()

# Ruta para poder iniciar sesion

@user_router.post('/login')
def login(user: User):
    if user.username == "admin" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content={"token": token})
    return JSONResponse(status_code=401, content={"message": "Invalid credentials"})

# Rutas para poder gets, posts y eso de users
