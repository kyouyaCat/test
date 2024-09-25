import streamlit as st
import pandas as pd
import numpy as np

# 初期化: ステートに変数がなければ設定する
if 'uploaded_photos' not in st.session_state:
    st.session_state.uploaded_photos = []

def task():
    st.header("課題曲")
    st.image("photo/e7badc37466ded77.png")
    st.text("曲名:")
    st.text("難易度:Master")
    st.text("レベル:13")
def mach():
    # 対戦相手とスコアのデータをプログラム内で定義
    data = [
        {"対戦相手": "Player A", "スコア1": 85, "スコア2": 90, "相手": "Player B"},
        {"対戦相手": "Player B", "スコア1": 70, "スコア2": 80, "相手": "Player A"},
        {"対戦相手": "Player C", "スコア1": 95, "スコア2": 85, "相手": "Player D"},
        {"対戦相手": "Player D", "スコア1": 65, "スコア2": 75, "相手": "Player C"}
    ]

    # DataFrameに変換して表示
    df = pd.DataFrame(data)
    st.table(df)

# Streamlitのタブ設定
tab1, tab2, tab3,tab4 = st.tabs(["概要","課題曲", "対戦相手", "結果"])

with tab1:
    st.header("大会概要")
with tab2:
    task()
with tab3:
    st.header("対戦相手")
    mach()
with tab4:
    st.header("結果")
    # 結果タブの内容をここに追加してください。
    