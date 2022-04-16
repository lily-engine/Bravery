from flask import Flask, render_template, request, url_for, redirect
import math

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/question', methods=['GET'])
def get():
	question_lists = ["HTML","CSS","JavaScript","JavaScriptのフレームワーク","バックエンドの言語","バックエンドのフレームワーク","Linux","Git/GitHub","Webの仕組み","MySQL/SQL","ポートフォリオ作成"]
	return render_template('question.html', \
		title = '診断しよう！', \
		message = '勉強したことがある項目を選択してみてね',
		question_lists = question_lists
	)

@app.route('/result', methods=['POST'])
def post():
	checkbox = request.form.getlist('checkbox')
	checkbox_count = len(checkbox)
	percentage = math.floor(checkbox_count / 10 * 100)
	return render_template('result.html', \
		title = '診断結果', \
		checkbox_count = checkbox_count, \
		checkbox = checkbox, \
		percentage = percentage)

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