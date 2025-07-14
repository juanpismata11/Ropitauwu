#pip install sqlalchemy
#pip install pymysql


from fastapi import FastAPI, Request, HTTPException
from fastapi.security import HTTPBearer
from config.database import  engine, Base


app = FastAPI()
app.title = "Mi primera API con FastAPIoasciwdbipwrirsbv"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)
