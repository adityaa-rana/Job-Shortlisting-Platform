from typing import Annotated
from pydantic import BaseModel,Field


class roadmapTaskResponseSchema(BaseModel):

    model_config = {"from_attributes": True}
    id: Annotated[int,Field(title="Task id")]
    application_id: Annotated[int,Field(title="Application id")]
    task: Annotated[str,Field(title="Task")]
    completed: Annotated[bool,Field(title="Task completion status")]


class updateTaskSchema(BaseModel):

    completed: Annotated[bool,Field(title="Completed")]