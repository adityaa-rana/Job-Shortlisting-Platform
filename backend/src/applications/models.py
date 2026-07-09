from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from src.utils.db import Base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,Float

class applicationModel(Base):
    __tablename__="application_table"
    id = Column(Integer, primary_key=True)
    candidate_id=Column(Integer,ForeignKey("user_table.id"),nullable=False)
    job_id= Column(Integer,ForeignKey("job_table.id"),nullable=False)
    resume_id= Column(Integer,ForeignKey("resume_table.id"),nullable=False)

    # by default false until changed by recruiter
    status   = Column(String,nullable=False,default="Applied")




    recruiter_message = Column(String,default=None)  
    created_at = Column(DateTime, default=datetime.utcnow)

    # from calculate ats score 
    ats_score=Column(Float,default=0)

    missing_skills = Column(String, nullable=True)
    learning_roadmap = Column(String, nullable=True)