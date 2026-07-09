from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from src.utils.db import Base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey

class jobModel(Base):
    __tablename__="job_table"
    id = Column(Integer, primary_key=True)
    title = Column(String,nullable=False)
    description = Column(String,nullable=False)
    experience_level = Column(String,nullable=False) # string? ("Fresher", "1-3 years", etc.)
    created_at = Column(DateTime, default=datetime.utcnow) # Foreign key to users table
    recruiter_id=Column(Integer,ForeignKey("user_table.id"),nullable=False)
    # from uploaded resume
    job_file_path=Column(String,nullable=True)
    
    # from extract_text function
    jd_text=Column(String,nullable=True)

    # from extract_skills function
    jd_skills=Column(String,nullable=True)
