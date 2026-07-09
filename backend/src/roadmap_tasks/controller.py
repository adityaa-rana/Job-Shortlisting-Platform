from sqlalchemy.orm import Session
from src.roadmap_tasks.models import roadmapTaskModel

def get_tasks(
    application_id:int,
    db:Session
):

    return db.query(
        roadmapTaskModel
    ).filter(
        roadmapTaskModel.application_id==
        application_id
    ).all()


def update_task(
    task_id:int,
    completed:bool,
    db:Session
):

    task=db.query(
        roadmapTaskModel
    ).filter(
        roadmapTaskModel.id==
        task_id
    ).first()

    # set the value as given by the frontend put input from checkbox
    task.completed=completed

    db.commit()

    db.refresh(task)

    return task