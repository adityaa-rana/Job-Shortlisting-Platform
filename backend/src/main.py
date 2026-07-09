from fastapi import FastAPI
from src.users.router import user_routes
from src.jobs.router import job_routes
from src.applications.router import application_routes
from src.interview_questions.router import question_routes
from src.resumes.router import resume_routes
from src.utils.db import Base
from src.utils.db import engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.roadmap_tasks.router import task_routes
from src.interview_questions.router import question_routes

app=FastAPI()
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(engine)

@app.get("/")
def greet():
    return {"Greetings":"Welcome to the site"}

app.include_router(user_routes)
app.include_router(job_routes)
app.include_router(application_routes)
app.include_router(resume_routes)
app.include_router(question_routes)
app.include_router(task_routes)