from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from src.utils.db import Base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey

class resumeModel(Base):
    __tablename__="resume_table"
    id = Column(Integer, primary_key=True)
    candidate_id= Column(Integer,ForeignKey("user_table.id"),nullable=False)
    file_path = Column(String,nullable=False)
    extracted_text = Column(String) 
    extracted_skills = Column(String) 
    created_at = Column(DateTime, default=datetime.utcnow) 


