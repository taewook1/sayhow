from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))

    questions = relationship("Question", back_populates="owner")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="questions")

    answers = relationship("Answer", back_populates="question")

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # ✅ 이거 추가
    created_at = Column(DateTime, default=datetime.utcnow)
    vote_score = Column(Integer, default=0)
    ai_feedback = Column(Text, nullable=True)

    question = relationship("Question", back_populates="answers")
    user = relationship("User")