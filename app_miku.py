import streamlit as st
import openai
import os
from datetime import datetime


# テキスト入力
url = st.text_input('URLを入力してください')

# ボタン
if st.button('ポジティブ化する'):
    st.write(url,'をポジティブ化します。')
    
    #URL
    openai.api_key = os.getenv("OPENAI_API_KEY")
    model_name = "gpt-4"

    prompt = url + "の内容をポジティブにしてください"
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    st.write("ポジティブ")
    print(response.choices[0]["message"]["content"].strip())





