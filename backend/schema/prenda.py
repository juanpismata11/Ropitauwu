from pydantic import BaseModel
from typing import Optional

class Prenda(BaseModel):
    id: Optional[int] = None 
    nombre: str
    img: str
    tipo: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "PLayera Zara",
                "password": "playera.jpeg",
                "tipo": "playera"
            }
        }