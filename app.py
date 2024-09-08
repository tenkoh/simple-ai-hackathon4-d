#####IMPORT###################################################
import os
import requests

from bs4 import BeautifulSoup
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

#####METHOD###################################################
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

#####MAIN###################################################
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



# テキスト入力
url = st.text_input("URLを入力してください。")

# 言語を選ばせたい
language = st.selectbox(
    '出力言語を選択してください。\nPlease choose the output language.',
    ('日本語', '英語', '中国語')
)

# ポジティブボタン押下処理
if st.button("ポジティブ化する💖"):
    #　GPTへ渡す情報
    model_name = "gpt-4o-mini"
    role="あなたはプロの心理カウンセラーです。\n"
    prompt = f'''以下の手順で、記事の内容をポジティブにしてください。
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
{get_article_body(url)}
'''
    
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

