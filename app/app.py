from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/question', methods=['GET'])
def get():
	question_lists = ["HTML","CSS","JavaScript","JavaScriptのフレームワーク","バックエンドの言語","バックエンド言語のフレームワーク","Linux","Git/GitHub","Webの仕組み","MySQL/SQL","ポートフォリオ作成"]
	return render_template('question.html', \
		title = '診断するよ', \
		message = 'どの勉強が終わっている？',
		question_lists = question_lists
	)

@app.route('/result', methods=['POST'])
def post():
	name = request.form.getlist('checkbox')
	return render_template('result.html', \
		title = '診断結果', \
		message = '{}の勉強が終わっているんですね！'.format('と'.join(name)))

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