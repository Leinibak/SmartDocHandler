from flask import Flask, render_template, request, redirect, url_for,send_file,send_from_directory
import os
import requests


# # static_folder와 static_url_path를 함께 지정하여 Flask가 정적 파일을 올바르게 찾도록 설정
app = Flask(__name__, static_folder="static", static_url_path="/static")

# Ensure output folder exists
OUTPUT_FOLDER = os.path.join(os.getcwd(), 'invoices_output')
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/<filename>')
def download_excel(filename):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    try:
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return {'error': 'File not found'}, 404
    except Exception as e:
        return {'error': str(e)}, 500


if __name__ == '__main__':
    app.run(port=8080, debug=True)
