import os

import requests
import streamlit as st
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_article_title(url):
    # URLからコンテンツを取得
    response = requests.get(url)

    # レスポンスが成功したか確認
    if response.status_code == 200:
        # HTMLコンテンツを解析
        soup = BeautifulSoup(response.text, "html.parser")

        # 'article_title'クラスを持つdiv要素を検索
        article_title = soup.find("h1", class_=["sc-uzx6gd-1", "lljVgU"])

        if article_title:
            # div要素の内容を返す
            return article_title.get_text(strip=True)
        else:
            return "Article title not found."
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"


def get_article_body(url):
    # URLからコンテンツを取得
    response = requests.get(url)

    # レスポンスが成功したか確認
    if response.status_code == 200:
        # HTMLコンテンツを解析
        soup = BeautifulSoup(response.text, "html.parser")

        # 'article_body'クラスを持つdiv要素を検索
        article_body = soup.find("div", class_="article_body")

        if article_body:
            # div要素の内容を返す
            return article_body.get_text(separator="\n\n", strip=True)
        else:
            return "Article body not found."
    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"


# テキスト入力
url = st.text_input("URLを入力してください")

# ボタン
if st.button("ポジティブ化する"):
    title = get_article_title(url)
    st.write(title, "をポジティブ化します。")

    # URL
    model_name = "gpt-4o-mini"
    # get_article_title(url)

    original = get_article_body(url)

    role = "あなたはプロの心理カウンセラーです。\n"
    prompt = f"""記事の内容をポジティブにしてください。過激な表現やグロテスクな表現は避けてください。見出しなどを付けずに修正後の文章のみ出力してください。Let's think step by step.
## 記事
{original}
"""
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt},
        ],
    )
    result = response.choices[0].message.content.strip()
    # st.title("ポジティブ")
    # st.write(response.choices[0].message.content.strip())

    # 2つの列を作成
    col1, col2 = st.columns(2)

    # 左側の列に表示する内容
    with col1:
        st.header("原文")
        st.markdown(original)

    # 右側の列に表示する内容
    with col2:
        st.header("ポジティブ")
        st.markdown(result)
