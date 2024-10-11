from smart_doc_handler.services.pdf_service.invoice.domestic_invoice import DomesticInvoice
# 다른 Invoice 클래스들도 여기에 임포트
# from .foreign_invoice import ForeignInvoice
# from .payable_invoice import PayableInvoice
# from .receivable_invoice import ReceivableInvoice
# from .credit_invoice import CreditInvoice

class InvoiceManager:
    def __init__(self, invoice_type, pdf_path):
        self.invoice_type = invoice_type
        self.pdf_processor = PDFProcessor(pdf_path)

    def process_invoice(self):
        text = self.pdf_processor.extract_text()

        if self.invoice_type == "domestic":
            invoice = DomesticInvoice(text)
        # elif self.invoice_type == "foreign":
        #     invoice = ForeignInvoice(text)
        # elif self.invoice_type == "payable":
        #     invoice = PayableInvoice(text)
        # elif self.invoice_type == "receivable":
        #     invoice = ReceivableInvoice(text)
        # elif self.invoice_type == "credit":
        #     invoice = CreditInvoice(text)
        else:
            raise ValueError("Unsupported Invoice Type")

        return invoice.extract_data()

# PDFProcessor 클래스가 필요하므로 아래에 import 추가
from smart_doc_handler.services.pdf_service.pdf_processor import PDFProcessor
