from services.pdf_service.excel_exporter import ExcelExporter
from services.pdf_service.invoice.our_company.domestic_invoice import DomesticInvoice

def test_excel_export():
    data = {
        'invoice_number': '12345',
        'date': '2023-01-01',
        'total_amount': '1000'
    }
    invoice = DomesticInvoice(data)
    exporter = ExcelExporter()
    result = exporter.export_to_excel([invoice])
    assert result is None  # 엑셀 저장이 성공적으로 되었는지 확인
