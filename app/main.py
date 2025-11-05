from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
import schemas
import models
from utils import perform_translation
import crud
from database import get_db, engine, Base
from typing import List


Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate", response_model=schemas.TaskResponse)
def translate(request: schemas.TranslationRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    # create DB task
    task = crud.create_translation_task(db, request.text, request.languages)

    # schedule background work WITHOUT passing the DB Session object
    background_tasks.add_task(perform_translation, task.id, request.text, request.languages)

    return {"task_id": task.id}

@app.get("/translate/{task_id}", response_model=schemas.TranslationStatus)
def get_translate(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_translation_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="task not found")

    return {
        "task_id": task.id,
        "status": task.status,
        "translation": task.translation
    }
