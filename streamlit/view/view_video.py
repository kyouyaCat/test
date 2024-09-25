import streamlit as st
import os
import win32com.client

# 検索関数の定義
def filter_videos(video_files, search_query):
    if search_query:
        filtered_video_files = [f for f in video_files if search_query.lower() in f.lower()]
    else:
        filtered_video_files = video_files
    return filtered_video_files

# タイトルの設定
st.title("動画閲覧アプリ")

# 動画が格納されているディレクトリ
video_directory = r"D:\新しいフォルダー\001\002\004\005\ahpic"

# ショートカット解決用の関数
def resolve_shortcut(shortcut_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    target_path = shortcut.Targetpath
    return shortcut.Description, target_path

# ディレクトリ内の動画ファイルリストを取得（ショートカットも解決）
video_files_info = []
for f in os.listdir(video_directory):
    if f.endswith(('mp4', 'avi', 'mov', 'mkv')):
        video_files_info.append((f, f))
    elif f.endswith('.lnk'):  # ショートカットの場合
        shortcut_path = os.path.join(video_directory, f)
        shortcut_name, target_path = resolve_shortcut(shortcut_path)
        if os.path.exists(target_path) and target_path.endswith(('mp4', 'avi', 'mov', 'mkv')):
            video_files_info.append((f, target_path))

# 検索ボックスの追加
search_query = st.text_input("検索キーワードを入力してください:")

# 動画をフィルタリング
filtered_video_files = filter_videos([f[0] for f in video_files_info], search_query)

# 検索結果の確認
if not filtered_video_files:
    st.warning("該当する動画がありません。")
else:
    # 動画選択のためのセレクトボックス
    selected_video = st.selectbox("表示する動画を選択してください:", [""] + filtered_video_files)

    # 動画が選択されている場合に表示
    if selected_video:
        video_info = next(info for info in video_files_info if info[0] == selected_video)
        video_path = video_info[1]  # 修正: ショートカット解決後のパスを使う

        try:
            # Streamlitのvideo関数を使って動画を表示
            st.video(video_path)
            # キャプションを表示
            st.text(video_info[0])
        except FileNotFoundError:
            st.error("指定されたパスに動画が見つかりません。")
        except Exception as e:
            st.error(f"動画の読み込み中にエラーが発生しました: {e}")
