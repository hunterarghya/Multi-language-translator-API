from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.orm import declarative_base

from app.database import Base

# Base = declarative_base()


class TranslationTask(Base):
    __tablename__ = "translation_tasks"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    languages = Column(JSON, nullable=False)  # list of languages
    status = Column(
        String(30), default="pending"
    )  # pending, in_progress, completed, failed
    translation = Column(
        JSON, nullable=True
    )  # dict mapping language to translated text
