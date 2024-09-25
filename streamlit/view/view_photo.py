import streamlit as st
from PIL import Image
import os

# 検索関数の定義
def filter_photos(photo_files, search_query):
    if search_query:
        filtered_photo_files = [f for f in photo_files if search_query.lower() in f.lower()]
    else:
        filtered_photo_files = photo_files
    return filtered_photo_files



# 写真が格納されているディレクトリ
photo_directory = r"D:\新しいフォルダー\001\002\004\005\ahpic\picfa"

# ディレクトリ内の写真ファイルリストを取得
photo_files = [f for f in os.listdir(photo_directory) if f.endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]

# 検索ボックスの追加
search_query = st.text_input("検索キーワードを入力してください:")

# 写真をフィルタリング
filtered_photo_files = filter_photos(photo_files, search_query)

# 検索結果の確認
if not filtered_photo_files:
    st.warning("該当する写真がありません。")
else:
    # 写真選択のためのセレクトボックス
    selected_photo = st.selectbox("表示する写真を選択してください:", [""] + filtered_photo_files)

    # 写真が選択されている場合に表示
    if selected_photo:
        photo_path = os.path.join(photo_directory, selected_photo)
        try:
            # PILを使って写真を読み込む
            image = Image.open(photo_path)
            # 写真を表示
            st.image(image, caption='表示中の写真', use_column_width=True)
        except FileNotFoundError:
            st.error("指定されたパスに写真が見つかりません。")
        except Exception as e:
            st.error(f"写真の読み込み中にエラーが発生しました: {e}")
