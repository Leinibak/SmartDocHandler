from services.pdf_service.invoice.our_company.domestic_invoice import DomesticInvoice

def test_domestic_invoice_extraction():
    data = {
        'invoice_number': '12345',
        'date': '2023-01-01',
        'total_amount': '1000'
    }
    invoice = DomesticInvoice(data)
    result = invoice.extract()
    assert result['invoice_number'] == '12345'
    assert result['total_amount'] == '1000'
