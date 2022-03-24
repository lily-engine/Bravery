from flask import Flask, render_template
from app import app

app = Flask(__name__)

@app.route('/')
def index():
    question_lists = ["HTML","CSS","JavaScript","JavaScriptのフレームワーク","バックエンドの言語","バックエンド言語のフレームワーク","Linux","Git/GitHub","Webの仕組み","MySQL/SQL","ポートフォリオ作成"]
    return render_template('view.html',
        title = '目指せエンジニア！学習到達度チェッカー',
        message = '学習済の項目にチェックを入れてください。',
        question_lists = question_lists
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)