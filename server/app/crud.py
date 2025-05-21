
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime


# 질문 함수

def create_question(db: Session, question: schemas.QuestionCreate, user_id: int):
    db_question = models.Question(
        title=question.title,
        content=question.content,
        user_id=user_id,
        created_at=datetime.utcnow()
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_question_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Question).offset(skip).limit(limit).all()


def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()




# 답변 함수

def create_answer(db: Session, answer: schemas.AnswerCreate, user_id: int):
    db_answer = models.Answer(
        content=answer.content,
        question_id=answer.question_id,
        user_id=user_id,
        created_at=datetime.utcnow(),
        vote_score=0,
        ai_feedback=None  # AI 피드백은 나중에 업데이트 가능
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def get_answers_for_question(db: Session, question_id: int, limit: int = 10):
    return (
        db.query(models.Answer)
        .filter(models.Answer.question_id == question_id)
        .order_by(models.Answer.vote_score.desc())
        .limit(limit)
        .all()
    )