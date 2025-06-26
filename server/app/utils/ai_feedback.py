from app.utils.usage_check import get_current_month_usage_usd
from app.models import FeedbackCache
from sqlalchemy.orm import Session
import openai
import os
import hashlib
from datetime import datetime
from dotenv import load_dotenv
import traceback

# 환경 변수 로드 및 API 키 설정
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_feedback(answer_text: str, question_text: str, db: Session) -> str:
    # ✅ 해시 키 생성 (질문 + 답변 기준)
    combined = question_text + answer_text
    hash_key = hashlib.sha256(combined.encode()).hexdigest()

    # ✅ 캐시 조회
    cached = db.query(FeedbackCache).filter(FeedbackCache.hash_key == hash_key).first()
    if cached:
        print("🎯 캐시 HIT")
        return cached.ai_feedback

    # ✅ GPT 사용량 체크
    current_usage = get_current_month_usage_usd()
    if current_usage >= 20.0:
        print(f"⛔ GPT 사용 차단됨. 현재 사용량: ${current_usage}")
        return "현재 AI 피드백 호출이 일시 중단되었습니다. (월 GPT 사용 한도 초과)"

    # ✅ GPT 프롬프트 구성
    prompt = f"""
아래는 누군가가 고민 상황에 대해 질문한 내용과, 이에 대한 다른 사람의 답변입니다.

이 답변은 어떤 말투(예: 유머, 직설, 무심함, 다정함 등)로 보이는지, 그리고 질문자가 이 말을 들었을 때 어떤 감정이 들 수 있을지를 구체적으로 설명해 주세요.

또한 이 답변이 가진 **장점**과 **한계/주의할 점**을 균형 있게 짚어주세요. (예: “이렇게 말하면 친구가 오히려 긴장하고 진지하게 받아들일 수 있다” vs “농담처럼 들릴 수도 있어 진심 전달이 어려울 수 있다”)

가능하다면 이 답변을 조금 더 세련되게 바꾸는 방법도 한 줄 정도 제안해 주세요.  
총 2~3문장 이내로 간결하게, **현실적인 분석**과 **센스 있는 제안**을 포함해 작성해 주세요.


[질문]
{question_text}

[답변]
{answer_text}

[AI 피드백]
    """

    try:
        # ✅ GPT 호출
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=250
        )

        feedback = response.choices[0].message["content"].strip()

        # ✅ 캐시 저장
        new_cache = FeedbackCache(
            hash_key=hash_key,
            ai_feedback=feedback,
            created_at=datetime.utcnow()
        )
        db.add(new_cache)
        db.commit()

        return feedback

    except Exception as e:
        print("🛑 GPT 호출 실패:")
        traceback.print_exc()
        return "AI 피드백을 생성하는 중 오류가 발생했습니다. 일시적인 문제일 수 있으니 잠시 후 다시 시도해 주세요."
