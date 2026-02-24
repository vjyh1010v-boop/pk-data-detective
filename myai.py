# 구글 제미나이 AI 더 심화
from google import genai
from dotenv import load_dotenv
import os

load_dotenv() # .env 파일로드
data = os.getenv("GEMINI_API_KEY")

def gai(que):
    client = genai.Client(api_key = data)
    response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents = que)
    print(response.text)

if __name__=="__main__":
    for n in range(5):
        gai(input("질문하세요."))