from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from src.utils.db import getdb

from src.roadmap_tasks import controller

from src.roadmap_tasks.dtos import (
    roadmapTaskResponseSchema,
    updateTaskSchema
)

task_routes=APIRouter(
    prefix="/tasks"
)

@task_routes.get(
    "/{application_id}",
    response_model=list[
        roadmapTaskResponseSchema
    ]
)
def get_tasks(
    application_id:int,
    db:Session=Depends(getdb)
):

    return controller.get_tasks(
        application_id,
        db
    )


@task_routes.put(
    "/{task_id}",
    response_model=
    roadmapTaskResponseSchema
)
def update_task(
    task_id:int,
    body:updateTaskSchema,
    db:Session=Depends(getdb)
):

    return controller.update_task(
        task_id,
        body.completed,
        db
    )