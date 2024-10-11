# tests/test_invoice_extract.py

import pytest
from smart_doc_handler.services.pdf_service.invoice.domestic_invoice import DomesticInvoice

def test_domestic_invoice_extract(sample_text):
    invoice = DomesticInvoice(sample_text)
    data = invoice.extract_data()
    assert data['invoice_number'] == '123456', "Invoice 번호가 올바르게 추출되지 않았습니다."
    assert data['total_amount'] == '1000.00', "총액이 올바르게 추출되지 않았습니다."
