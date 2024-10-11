from flask import Flask, request, jsonify, send_from_directory, render_template
from services.pdf_service.pdf_processor import PDFProcessor
import os

app = Flask(__name__)

@app.route('/')
def home():
    # 프론트엔드의 'index.html'을 렌더링
    return send_from_directory(os.path.join(os.path.dirname(__file__), '../frontend/templates/'), 'index.html')


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
