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

    prompt = url + "の内容をポジティブにしてください"
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    st.write("ポジティブ")
    print(response.choices[0].message.content.strip())
