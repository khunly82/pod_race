from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

class Base(DeclarativeBase):
    pass

engine = create_engine(url=os.getenv('DB_URL'))
session_maker = sessionmaker(bind=engine)

def get_session():
    try:
        session = session_maker()
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()