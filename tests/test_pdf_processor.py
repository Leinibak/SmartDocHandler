# tests/test_pdf_processor.py

import pytest
from smart_doc_handler.services.pdf_service.pdf_processor import PDFProcessor

def test_extract_text(sample_pdf_path):
    processor = PDFProcessor(sample_pdf_path)
    text = processor.extract_text()
    assert "Invoice Number" in text, "텍스트 추출에 실패했습니다."
    assert "Total Amount" in text, "텍스트 추출에 실패했습니다."
