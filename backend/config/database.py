import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# Base de datos SQLite para la aplicacion FastAPI

sqlite_file_name = "../database.sqlite"

#estamos leyendo el directorio actual que es database.py
base_dir = os.path.dirname(os.path.abspath(__file__))

#creamos la url de la base de datos uniendp las 2 variables anteriores 
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url, echo = True)

Session = sessionmaker(bind=engine)

Base = declarative_base()