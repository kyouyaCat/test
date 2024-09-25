import streamlit as st
import os
import subprocess

# タイトルの設定
st.title("Pythonスクリプト起動アプリ")

# スクリプトが格納されているディレクトリ
script_directory = os.path.dirname(os.path.abspath(__file__))

# ディレクトリ内のPythonスクリプトファイルリストを取得
script_files = [f for f in os.listdir(script_directory) if f.endswith('.py') and f != os.path.basename(__file__)]

# スクリプト選択のためのセレクトボックス
selected_script = st.selectbox("実行するスクリプトを選択してください:", [""] + script_files)

# スクリプトが選択されている場合に実行
if selected_script:
    script_path = os.path.join(script_directory, selected_script)

    # ボタンを追加してスクリプトを実行
    if st.button("スクリプトを実行"):
        try:
            # サブプロセスを使ってスクリプトを実行
            result = streamlit.run(['python', script_path], capture_output=True, text=True)
            st.write("スクリプトの出力:")
            st.text(result.stdout)
            if result.stderr:
                st.write("スクリプトのエラー:")
                st.text(result.stderr)
        except Exception as e:
            st.error(f"スクリプトの実行中にエラーが発生しました: {e}")
