from flask import Flask, request, jsonify, send_from_directory, send_file
from services.pdf_service.invoice_manager import InvoiceManager  # InvoiceManager 사용
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Upload folder path
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
OUTPUT_FOLDER = os.path.join(os.getcwd(), 'invoices_output')

# Ensure that directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  # OUTPUT_FOLDER도 존재하도록 설정

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'xlsx', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return send_from_directory(os.path.join(os.path.dirname(__file__), '../frontend/templates/'), 'index.html')

# Route to handle file upload and PDF data extraction
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        return jsonify({'error': 'No files part in the request'}), 400

    files = request.files.getlist('files[]')
    client = request.form.get('client')
    doc_type = request.form.get('doc_type')
    region = request.form.get('region')

    print(client, doc_type, region)

    if not client or not doc_type or not region:
        return jsonify({'error': 'Missing form data (client, doc_type, region)'}), 400

    saved_files = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            saved_files.append(file_path)
        else:
            return jsonify({'error': 'File not allowed'}), 400

    # InvoiceManager를 사용하여 파일 처리
    invoice_manager = InvoiceManager()
    output_file = invoice_manager.process_invoices(client, doc_type, region, saved_files)

    return jsonify({'success': True, 'output_file': output_file}), 200

# Route to handle file download
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    try:
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return jsonify({'error': 'File not found or download error'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
