from typing import Annotated,Optional
from datetime import datetime
from pydantic import BaseModel,Field

class resumeResponseSchema(BaseModel):
    model_config = {"from_attributes": True}
    id: Annotated[int, Field(title="Resume   id")]
    candidate_id: Annotated[int, Field(title="Candidate id")]
    file_path: Annotated[str, Field(title="File path")]
    extracted_text: Annotated[Optional[str], Field(title="Extracted text",default=True)]
    extracted_skills: Annotated[Optional[str] , Field(title="Extracted skills",default=True)]
    created_at: Annotated[datetime, Field(title="Resume upload time")]
