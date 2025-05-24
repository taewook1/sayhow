from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import random
from datetime import datetime

from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter(prefix="/vote", tags=["Vote"])

# 랜덤 답변 2개 조회
@router.get("/pair", response_model=schemas.VotePairResponse)
def get_vote_pair(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    answers = db.query(models.Answer).filter(models.Answer.question_id == question_id).all()

    if len(answers) < 2:
        raise HTTPException(status_code=400, detail="투표할 답변이 2개 이상 필요합니다.")

    selected_answers = random.sample(answers, 2)
    return {"answers": selected_answers}


# 투표 처리 (중복 방지 + 예외 처리 추가)
@router.post("", response_model=schemas.VoteResultResponse)
def vote_for_answer(
    vote: schemas.VoteRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    answer = db.query(models.Answer).filter(models.Answer.id == vote.answer_id).first()

    if not answer:
        raise HTTPException(status_code=404, detail="해당 답변이 존재하지 않습니다.")

    try:
        # 중복 투표 기록 방지
        vote_record = models.VoteRecord(
            user_id=current_user.id,
            question_id=answer.question_id,
            voted_answer_id=answer.id,
            created_at=datetime.utcnow()
        )
        db.add(vote_record)

        # 투표 점수 증가
        answer.vote_score += 1
        db.commit()
        db.refresh(answer)

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="이미 이 질문에 투표하셨습니다.")

    return {"answer_id": answer.id, "new_vote_score": answer.vote_score}