from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None 
    username: str = Field(min_length=5, max_length = 30)
    password: str = Field(min_length=5, max_length = 50)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "juanpismata11",
                "password": "lalokura11",
            }
        }