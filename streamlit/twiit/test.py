import streamlit as st
import requests
from bs4 import BeautifulSoup

def vocalo_ranking():
    url = 'https://vocaloard.injpok.tokyo/?s=2'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.find_all("p")

    rh1 = [elem.text.strip() for elem in elems[3:]]
    rh1 = [line for line in rh1 if line]

    return "<br>".join(rh1)


coli,coli2 = st.columns(2)

with coli:
    st.image("photo/qDAYCz4A_400x400 (1).jpg",width=200)
    st.title("Kyouya")

with coli2:
    st.header("自己紹介")
    st.divider()
    st.write("ユーザー名 : @kyouyaCat1021")
    st.write("名前 : Kyouya")
    st.write("Twitter : https://twitter.com/kyouyaCat1021")
    

tab1, tab2,tab3 = st.tabs(["プロフィール","サブ垢の一部","メモ(ボカロランキング)"])

with tab1:
    st.header("プロフィール")
    st.write(" 2002/10/21猫の皮をかぶった人間にゃ maimaiメイン めっちゃ喋る....")
    st.write("それ以外はサブ垢にゃ～通してほしい人はdmでお願いにゃ")
    
    pro ="""こんにちは、Kyouyaと言います。
        音ゲーでmaimaiメインのツイートするアカウント,
        にゃーにゃー喋ってるキャラにゃwww
        平塚のラウンドワンで遊ぶのがほとんどで大学行くときは横浜、鶴見でやることがたまにいるかも
        ボッチでやることがほとんどでたまに地元でよく遊ぶ人とやったり、FFさんとも遊んだりすることもあるけど、正直人と遊ぶ方が楽しいしで絡み増やしたいわ...
        maimai意外で好きなのは、曲聞いたり、食べること、あと最近は忙しくてできてないけど推し活をしていたりってところ
        P丸様とすとぷりの莉犬くんを特に推してる、
        結構昔にグッズを集めて写真取ったこともあったりしたな～ってところ"
        どうぞよろしくお願いします"""
    
    st.markdown(pro)
    
    
with tab2:
    st.header("サブ垢の一部")
    st.markdown("こんな感じ～ってところ、通す人は選ぶけど興味あれば声かけてくれたら通すかも")
    
    colia,colib,colic = st.columns(3)
    with colia:
        st.image("photo/GN2TAwya4AAAvQ4.jpg",caption="場先の人と飲む〜乾杯🍻",width=200)
    with colib:
        st.image("photo/GOBTwYCbcAEAQzX.jpg",caption="帰宅途中に撮った謎写真、来年の予兆かな？",width=200)
    with colic:
        st.image("photo/GMzEvlxaoAAqTA3.jpg",caption="傘買った〜黒だと間違えられそうだし緑にしたけどめっちゃ良い色〜",width=200)
        
with tab3:
    vocalo_ranking_text = vocalo_ranking()
    st.markdown(vocalo_ranking_text, unsafe_allow_html=True)