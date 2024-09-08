import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from article import ArticleParser

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# テキスト入力
url = st.text_input("URLを入力してください")
article = ArticleParser(url).get_article_body()

# 言語を選ばせたい
language = st.selectbox(
    "出力言語を選択してください。\nPlease choose the output language.",
    ("日本語", "英語", "中国語"),
)

# ポジティブボタン押下処理
if st.button("ポジティブ化する💖"):
    # 　GPTへ渡す情報
    model_name = "gpt-4o-mini"
    role = "あなたはプロの心理カウンセラーです。\n"
    prompt = f"""以下の手順で、記事の内容をポジティブにしてください。
    【手順1】
    例えば、以下の様にポジティブな表現に変えてください。この時に、引用された発言は書き換えてはいけません。。
    ・「積極性に欠ける」は「控えめな性格」
    ・「頭が悪い」は「天然」
    ・「貧乏」は「清貧」
    ・「忙しい」は「充実している」
    Let's think step by step.
    【手順２】
    例えば、以下の様に過激な表現やグロテスクな表現は柔らかい表現に変更して下さい。
    ・「殺す」は「天国へ導いた」
    【手順4】
    見出しを「💗ポジティブ化したニュース💗」として、マークダウンの表示にしてください。
    見出しの次の行は「以下の内容をポジティブに変換しました～✨」と書いてください。
    その次の行で、「{url}」を出力してください。コードブロックにして、簡単にコピーできるようにしてください。
    その下に、ポジティブ化したニュースを出力してください。
    【手順4】
    出力言語は{language}にしてください。
    【手順5】
    ・出力言語が日本語の場合、語尾は「なんだよ♡」や「だよ」や「だって～！」とか「らしいよ✨」とかにしてください。
    ・出力言語が日本語以外の場合は「♡」とか「★」とか「😊」とか「💕」を使ってください。
    ・語尾が絵文字の時は「。」を削除してください。
    【手順7】
    最後に注意点です。{language}に直して表示してください。
## 記事
{article}
"""

    # API叩く
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt},
        ],
    )

    # 出力
    st.write(response.choices[0].message.content.strip())
