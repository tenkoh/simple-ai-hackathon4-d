import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from article import ArticleParser

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
{ArticleParser(url).get_article_body()}
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

