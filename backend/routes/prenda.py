from fastapi import APIRouter
#from jwt_manager import create_token
from fastapi.responses import JSONResponse
from schema.prenda import Prenda
from fastapi.encoders import jsonable_encoder
from config.database import Session
from services.prenda import PrendaService
from typing import List


prenda_router = APIRouter()

# Rutas para poder gets, posts y eso de prendas

@prenda_router.get('/prendas', response_model=List[Prenda], status_code=200)
def get_prendas():
    db = Session()
    result = PrendaService(db).get_prendas()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@prenda_router.get('/prendas/{id}', response_model=Prenda, status_code=200)
def get_prenda(id: int):
    db = Session()
    result = PrendaService(db).get_prenda_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "Prenda not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@prenda_router.post('/prendas', response_model = dict, status_code=201)
def create_prenda(prenda : Prenda):
    db = Session()
    PrendaService(db).create_prenda(prenda)
    return JSONResponse(status_code=201, content={"message": "Prenda created successfully"})

@prenda_router.put('/prendas/{id}', response_model = dict, status_code = 200)
def update_prenda(id: int, prenda: Prenda):
    db = Session()
    result = PrendaService(db).get_prenda_by_id(id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'Prenda not found'})
    PrendaService(db).update_prenda(id, prenda)
    return JSONResponse(status_code=200, content={"message": "Prenda updated successfully"})

@prenda_router.delete('/prendas/{id}', response_model = dict, status_code = 200)
def delete_prenda(id: int):
    db = Session()
    result = PrendaService(db).get_prenda_by_id(id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message': 'Prenda not found'})
    PrendaService(db).delete_prenda(id)
    return JSONResponse(status_code=200, content={"message": "Prenda deleted successfully"})