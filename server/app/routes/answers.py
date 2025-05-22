from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, crud, models
from app.database import get_db
from app.auth import get_current_user

router = APIRouter(prefix="/answers", tags=["answers"])


# 답변 작성 (로그인 필요)
@router.post("/", response_model=schemas.Answer)
def create_answer(
    answer: schemas.AnswerCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_answer(db, answer, current_user.id)


# 특정 질문에 달린 답변 목록 조회
@router.get("/question/{question_id}", response_model=List[schemas.Answer])
def get_answers_for_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_answers_for_question(db, question_id)