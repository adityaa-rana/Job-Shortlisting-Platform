from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from src.utils.db import Base


class roadmapTaskModel(Base):

    __tablename__="roadmap_tasks"

    id=Column(
        Integer,
        primary_key=True,
        index=True
    )

    application_id=Column(
        Integer,
        ForeignKey("application_table.id")
    )

    task=Column(String)

    completed=Column(
        Boolean,
        default=False
    )