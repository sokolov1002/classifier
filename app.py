from model import run_model
from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		result = run_model(request.form['img'])
		return render_template('index.html',result=result)

if __name__ == '__main__':
	app.run(debug=True)