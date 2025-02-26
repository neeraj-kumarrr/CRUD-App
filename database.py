
from sqlalchemy.orm import sessionmaker ,declarative_base
from sqlalchemy import create_engine

URL_DATABASE = "mysql+pymysql://root:neeraj123456@localhost:3306/blogapplication"

engine =create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()



