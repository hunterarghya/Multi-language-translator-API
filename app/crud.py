from sqlalchemy.orm import Session
import models
from datetime import datetime

def create_translation_task(db: Session, text: str, languages: list):
    task = models.TranslationTask(text=text, languages=languages, status="pending", translation=None)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_translation_task(db: Session, task_id: int):
    return db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()

def update_translation_task(db: Session, task_id: int, translation: dict):
    task = db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()
    if not task:
        return None
    task.translation = translation
    task.status = "completed"
    db.commit()
    db.refresh(task)
    return task

def set_task_in_progress(db: Session, task_id: int):
    task = db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()
    if not task:
        return None
    task.status = "in_progress"
    db.commit()
    db.refresh(task)
    return task

def set_task_failed(db: Session, task_id: int, message: str = None):
    task = db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()
    if not task:
        return None
    task.status = "failed"
    task.translation = {"error": message} if message else None
    db.commit()
    db.refresh(task)
    return task
