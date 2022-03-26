from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    question_lists = ["HTML","CSS","JavaScript","JavaScriptのフレームワーク","バックエンドの言語","バックエンド言語のフレームワーク","Linux","Git/GitHub","Webの仕組み","MySQL/SQL","ポートフォリオ作成"]
    return render_template('view.html',
        title = '目指せバックエンドエンジニア！学習到達度チェッカー',
        message = '学習済の項目にチェックを入れてください。学習の到達度を判定します！',
        question_lists = question_lists
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)