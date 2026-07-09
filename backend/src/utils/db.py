from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from src.utils.settings import settings


engine=create_engine(url=settings.DB_CONNECTION)

'''SQLAlchemy needs a way to know:

Which Python classes represent database tables.
What columns each table has.
How to create those tables in the database.

Base acts as the parent class for all your database models.'''
Base=declarative_base()
LocalSession = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def getdb():
    session=LocalSession()
    try:
        yield session
    finally:
        session.close()