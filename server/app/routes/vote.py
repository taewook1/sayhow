from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import random

from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter(prefix="/vote", tags=["Vote"])

# 랜덤 답변 2개 조회
@router.get("/pair", response_model=schemas.VotePairResponse)
def get_vote_pair(question_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    # 해당 질문에 연결된 답변 조회
    answers = db.query(models.Answer).filter(models.Answer.question_id == question_id).all()

    if len(answers) < 2:
        raise HTTPException(status_code=400, detail="투표할 답변이 2개 이상 필요합니다.")

    # 랜덤으로 2개 선택
    selected_answers = random.sample(answers, 2)
    return {"answers": selected_answers}


# 투표 처리
@router.post("", response_model=schemas.VoteResultResponse)
def vote_for_answer(vote: schemas.VoteRequest, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    answer = db.query(models.Answer).filter(models.Answer.id == vote.answer_id).first()

    if not answer:
        raise HTTPException(status_code=404, detail="해당 답변이 존재하지 않습니다.")

    # vote_score 증가
    answer.vote_score += 1
    db.commit()
    db.refresh(answer)

    return {"answer_id": answer.id, "new_vote_score": answer.vote_score}
