from crypt import methods
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def main():
    question_lists = ["HTML","CSS","JavaScript","JavaScriptのフレームワーク","バックエンドの言語","バックエンド言語のフレームワーク","Linux","Git/GitHub","Webの仕組み","MySQL/SQL","ポートフォリオ作成"]
    return render_template('index.html',
        title = 'ぴよぴよエンジニア診断🐣',
        message = 'バックエンドエンジニアになりたい人向け、学習項目のチェックリストです。学習済の項目にチェックを入れると、学習の到達度を判定します。',
        question_lists = question_lists
    )

@app.route('/terms')
def terms_of_service():
    return render_template('terms.html')

@app.errorhandler(404)
def redirect_top_page(error):
    return redirect(url_for('main'))

@app.errorhandler(500)
def redirect_top_page(error):
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)