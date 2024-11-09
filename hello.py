from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)					#exporting file name to FLASK_APP variable


@app.route('/')
def hello_world():
	return 'Hello, Peppe8o users!'

@app.route('/show_abfrage')
def show_abfrage():
    return render_template('abfrage.html')

@app.route('/process', methods=['POST'])
def process_form():
    url = request.form.get('url')
    print(f"url: {url}")
    return redirect(url_for('success', url=url))

@app.route('/success')
def success():
    url = request.args.get('url')
    return f"Vielen Dank, für die url: {url}!"


@app.route('/abfrage')
def test():
    liste=["www.google.de"]
    url=request.args.get('url')
    return render_template('abfrage.html', url=url)



