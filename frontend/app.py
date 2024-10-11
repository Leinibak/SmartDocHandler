from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        response = requests.post('http://localhost:5000/process_invoice', files={'file': file})
        return response.json()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8080, debug=True)
