from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timezone

from app import schemas, crud, models
from app.database import get_db
from app.auth import get_current_user
from app.utils.ai_feedback import generate_feedback

router = APIRouter(prefix="/answers", tags=["Answer"])


# 답변 작성 (로그인 필요)
@router.post("", response_model=schemas.AnswerResponse)
def create_answer(
    answer: schemas.AnswerCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    # ✅ 질문 내용 조회
    question = db.query(models.Question).filter(models.Question.id == answer.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="해당 질문이 존재하지 않습니다.")

    # ✅ GPT 피드백 생성 (질문 제목 + 본문과 함께 전달)
    question_text = f"{question.title}\n{question.content}"
    ai_feedback = generate_feedback(answer.content, question_text, db)

    # ✅ 답변 저장
    new_answer = models.Answer(
        content=answer.content,
        question_id=answer.question_id,
        user_id=current_user.id,
        created_at=datetime.now(timezone.utc),
        vote_score=0,
        ai_feedback=ai_feedback
    )
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)
    return new_answer

# 특정 질문에 달린 답변 목록 조회
@router.get("/question/{question_id}", response_model=List[schemas.Answer])
def get_answers_for_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_answers_for_question(db, question_id)