#pip install sqlalchemy
#pip install pymysql
#pip install uvicorn
#pip install fastapi

from fastapi import FastAPI, Request, HTTPException
from fastapi.security import HTTPBearer
from config.database import  engine, Base
from routes.user import user_router
from routes.prenda import prenda_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.title = "Mi primera API con FastAPIoasciwdbipwrirsbv"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)
app.include_router(user_router)
app.include_router(prenda_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)