import pytest
from services.pdf_service.pdf_processor import PDFProcessor

def test_pdf_processing():
    processor = PDFProcessor("test_invoice","pdf" )
    result = processor.process()
    assert result is not None
