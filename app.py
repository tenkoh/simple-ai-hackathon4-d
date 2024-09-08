import os
import requests

from bs4 import BeautifulSoup
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_article_body(url):
    # URLからコンテンツを取得
    response = requests.get(url)
    
    # レスポンスが成功したか確認
    if response.status_code == 200:
        # HTMLコンテンツを解析
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 'article_body'クラスを持つdiv要素を検索
        article_body = soup.find('div', class_='article_body')
        
        if article_body:
            # div要素の内容を返す
            return article_body.get_text(strip=True)
        else:
            return "Article body not found."
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"

# テキスト入力
url = st.text_input("URLを入力してください")

# ボタン
if st.button("ポジティブ化する"):
    st.write(url, "をポジティブ化します。")

    # URL
    model_name = "gpt-4o-mini"

    role="あなたはプロの心理カウンセラーです。\n"
    prompt = f'''記事の内容をポジティブにしてください。過激な表現やグロテスクな表現は避けてください。Let's think step by step.
## 記事
{get_article_body(url)}
'''
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt},
        ],
    )

    st.title("ポジティブ")
    st.write(response.choices[0].message.content.strip())

