from flask import Flask, request, jsonify, send_from_directory
from smart_doc_handler.services.pdf_service.invoice_manager import InvoiceManager
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '../../frontend/uploads/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), '../../frontend/templates/'), 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    invoice_type = request.form.get('invoice_type')

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(save_path)

    # Invoice 처리
    manager = InvoiceManager(invoice_type, save_path)
    try:
        extracted_data = manager.process_invoice()
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    return jsonify(extracted_data)

if __name__ == "__main__":
    app.run(debug=True)
