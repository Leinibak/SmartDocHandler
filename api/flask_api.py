from flask import Flask, request, jsonify, send_from_directory, render_template,send_file
from services.pdf_service.pdf_processor import PDFProcessor 
from services.pdf_service.excel_exporter import ExcelExporter
from services.pdf_service.pattern_manager import PatternManager 

from werkzeug.utils import secure_filename
from services.pdf_service.invoice_manager import InvoiceManager
import os

app = Flask(__name__)


# Upload folder path
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
OUTPUT_FOLDER = os.path.join(os.getcwd(), 'invoices_output')

# Ensure that directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'xlsx', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    # 프론트엔드의 'index.html'을 렌더링
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

    # Retrieve patterns from the database using the provided client, doc_type, and region
    patternmanager =PatternManager()
    patterns = patternmanager.get_pattern(client, doc_type, region)

    # Process the uploaded PDF files
    pdf_processor = PDFProcessor(client, doc_type, region)
    extracted_data = pdf_processor.process_files(saved_files, patterns)  # Pass the patterns here

    # Export extracted data to Excel
    output_filename = 'invoices_output.xlsx'
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
    excel_exporter = ExcelExporter()
    excel_exporter.export_to_excel(extracted_data, output_path)

    return jsonify({'success': True, 'output_file': output_filename}), 200



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


@app.route('/process_invoice', methods=['POST'])
def process_invoice():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filepath = f"./uploads/{file.filename}"
    file.save(filepath)

    # PDF 파일 처리
    processor = PDFProcessor(filepath)
    processor.process()

    return jsonify({"message": "Invoice processed successfully"})

if __name__ == '__main__':
    app.run(debug=True)


 