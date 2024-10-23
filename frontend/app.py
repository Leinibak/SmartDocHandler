from flask import Flask, render_template, request, redirect, url_for,send_file
import os
import requests

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload():
#     file = request.files['file']
#     if file:
#         response = requests.post('http://localhost:5000/process_invoice', files={'file': file})
#         return response.json()
#     return redirect(url_for('index'))

# @app.route('/download/<filename>')
# def download_excel(filename):
#     return send_file(f'../invoices_output/{filename}', as_attachment=True)



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
