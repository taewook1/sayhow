from app.utils.usage_check import get_current_month_usage_usd
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_feedback(answer_text: str, question_text: str) -> str:
    # ✅ GPT 호출 전 사용량 체크
    current_usage = get_current_month_usage_usd()
    if current_usage >= 20.0:
        print(f"⛔ GPT 사용 차단됨. 현재 사용량: ${current_usage}")
        return "현재 AI 피드백 호출이 일시 중단되었습니다. (월 GPT 사용 한도 초과)"

    # ✅ GPT 프롬프트 구성 및 호출
    prompt = f"""
아래는 어떤 사람이 고민 상황에 대해 질문한 내용과, 그에 대한 다른 사람의 답변입니다.

이 답변을 보고 답변자가 어떤 성향이나 말투를 가지고 있는지 파악하고, 상대방(질문자) 입장에서 어떻게 느껴질 수 있을지를 공감적으로 분석해 주세요.  
답변이 꼭 나쁘다는 평가보다는, 어떤 상황에서는 좋을 수 있고, 어떤 경우에는 조심해야 할 수 있다는 식으로 현실적인 조언을 포함해 주세요.  

그리고 가능하다면, 조금 더 부드럽게 말하거나 질문을 되묻는 방식으로 바꾼 예시도 간단히 제안해 주세요.  
총 2~3문장 이내로, 상대방을 배려하면서 분석적이고 따뜻한 피드백을 작성해 주세요.

[질문]
{question_text}

[답변]
{answer_text}

[AI 피드백]
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=250
        )
        return response.choices[0].message["content"].strip()

    except Exception as e:
        import traceback
        print("🛑 GPT 호출 실패:")
        traceback.print_exc()
        return "AI 피드백을 생성하는 중 오류가 발생했습니다. " "일시적인 문제일 수 있으니 잠시 후 다시 시도해 주세요."