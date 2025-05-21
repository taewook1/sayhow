from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud, models
from app.database import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/questions", tags=["questions"])


# 질문 작성
@router.post("/", response_model=schemas.Question)
def create_question(
    question: schemas.QuestionCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_question(db, question, current_user.id)


# 질문 목록 조회
@router.get("/", response_model=List[schemas.Question])
def list_questions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_question_list(db, skip=skip, limit=limit)


# 특정 질문 조회
@router.get("/{question_id}", response_model=schemas.Question)
def get_question_detail(question_id: int, db: Session = Depends(get_db)):
    question = crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question