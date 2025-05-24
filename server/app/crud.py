
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime
import random


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
        ai_feedback=None  # AI 피드백은 나중에
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


def get_two_random_answers(db: Session, question_id: int):
    answers = db.query(models.Answer).filter(models.Answer.question_id == question_id).all()
    if len(answers) < 2:
        return []
    return random.sample(answers, 2)


def vote_for_answer(db: Session, answer_id: int):
    answer = db.query(models.Answer).filter(models.Answer.id == answer_id).first()
    if not answer:
        return None
    answer.vote_score += 1
    db.commit()
    db.refresh(answer)
    return answer