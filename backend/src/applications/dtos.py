from pydantic import BaseModel,Field
from typing import Annotated,Optional
from datetime import datetime

class applyJobSchema(BaseModel):
    # these are the only 2 things that the candidate will have while applying
    job_id: Annotated[int, Field(title="Job id")]
    resume_id: Annotated[int, Field(title="Resume id")]


class applicationResponseSchema(BaseModel):
    model_config= {"from_attributes": True}
    id: Annotated[int, Field(title="Job id")]
    candidate_id: Annotated[int, Field(title="Candidate id")]
    job_id: Annotated[int, Field(title="Job id")]
    resume_id: Annotated[int, Field(title="Resume id")]
    status: Annotated[Optional[str], Field(title="Application status",default=None)]
    recruiter_message: Annotated[Optional[str], Field(title="Recruiter feedback",default=None)]
    created_at: Annotated[datetime, Field(title="Application creation time")]
    ats_score:Annotated[Optional[float],Field(title="ATS score",default=0)]
    missing_skills: Annotated[Optional[str], Field(title="Missing Skills", default=None)]
    learning_roadmap: Annotated[Optional[str],Field(title="Learning Roadmap",default=None )]


class updateApplicationSchema(BaseModel):
    status: Annotated[Optional[str], Field(title="Application status",default=None)]
    recruiter_message: Annotated[Optional[str], Field(title="Recruiter feedback",default=None)]