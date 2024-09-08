import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# テキスト入力
url = st.text_input("URLを入力してください")

# ボタン
if st.button("ポジティブ化する"):
    st.write(url, "をポジティブ化します。")

    # URL
    model_name = "gpt-4"

    role="あなたはプロの心理カウンセラーです。\n"
    prompt = url + "の内容をポジティブにしてください。過激な表現やグロテスクな表現は避けてください。Let's think step by step."
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": role + prompt},
        ],
    )

    #げんぶん
    prompt_g = "以下のURLの内容をそのまま出力してください\n" + url
    response_g = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt_g},
        ],
    )

    st.title("原文")
    st.write(response_g.choices[0].message.content.strip())

    st.title("ポジティブニュース")
    st.write(response.choices[0].message.content.strip())
    