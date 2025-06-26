from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth import get_current_user
from app.database import get_db
from app import models
import openai
import os

router = APIRouter(prefix="/me", tags=["MyPage"])

openai.api_key = os.getenv("OPENAI_API_KEY")

@router.get("/profile-analysis")
def get_profile_analysis(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    user_id = current_user.id

    # 질문과 답변 불러오기
    questions = db.query(models.Question).filter(models.Question.user_id == user_id).all()
    answers = db.query(models.Answer).filter(models.Answer.user_id == user_id).all()

    if not questions and not answers:
        raise HTTPException(status_code=404, detail="분석할 질문/답변이 없습니다.")

    # 분석 대상 문자열 구성
    examples = []
    for q in questions:
        examples.append(f"Q: {q.title} - {q.content}")
    for a in answers:
        examples.append(f"A: {a.content}")

    combined = "\n".join(examples[:10])  # 너무 길면 10개까지만

    # GPT 프롬프트
    prompt = f"""
아래는 한 사용자가 작성한 질문과 답변입니다. 이 사용자의 말투, 성향, 대화 태도를 종합적으로 분석해 주세요.

- 어떤 스타일로 소통하는 사람인지
- 장점과 주의할 점은 무엇인지
- 대화를 더 잘하기 위해 참고할 점

총 3~5문장 이내로, 명확하고 센스 있게 작성해 주세요.

[사용자 질문/답변 예시]
{combined}

[AI 피드백]
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        ai_feedback = response.choices[0].message["content"].strip()
        return {"feedback": ai_feedback}

    except Exception as e:
        print("🛑 GPT 호출 실패:", e)
        raise HTTPException(status_code=500, detail="GPT 분석 중 오류 발생")
