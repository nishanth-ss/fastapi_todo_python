## sqlalchemy is the python library used to interact with database
## create_engine is a function that creates a connection engine for your database
from sqlalchemy import create_engine;
## sessionmaker - creates database session, A session allows you to perform database operations such as INSERT,UPDATE,DELETE AND SELECT
## declarative_base - create a base class for defining database model, your database model classes will inherit from this base class 
from sqlalchemy.orm import sessionmaker, declarative_base;
from dotenv import load_dotenv;
import os;
load_dotenv();
DATABASE_URL=os.getenv("DATABASE_URL");
engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()