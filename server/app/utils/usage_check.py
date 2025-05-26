import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_current_month_usage_usd() -> float:
    try:
        now = datetime.utcnow()
        start_date = now.replace(day=1).strftime("%Y-%m-%d")
        end_date = now.strftime("%Y-%m-%d")

        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }

        url = f"https://api.openai.com/v1/dashboard/billing/usage?start_date={start_date}&end_date={end_date}"
        response = requests.get(url, headers=headers)
        data = response.json()
        return round(data.get("total_usage", 0) / 100.0, 2)  # 단위: USD
    except Exception as e:
        print("💥 Usage API 호출 실패:", e)
        return 0.0  # 실패 시 0으로 간주