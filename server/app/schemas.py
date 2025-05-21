from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# 사용자 스키마
class UserBase(BaseModel):
    username: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# 질문 스키마
class QuestionBase(BaseModel):
    title: str
    content: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True


# 답변 스키마
class AnswerBase(BaseModel):
    content: str

class AnswerCreate(AnswerBase):
    question_id: int

class Answer(AnswerBase):
    id: int
    question_id: int
    user_id: int
    created_at: datetime
    vote_score: int
    ai_feedback: Optional[str] = None

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str