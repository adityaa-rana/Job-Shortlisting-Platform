from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.utils.db import Base

class UserModel(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # username = Column(String, nullable=False)
    email = Column(String,nullable=False,unique=True)
    hash_password = Column(String, nullable=False)
    role = Column(String,nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)