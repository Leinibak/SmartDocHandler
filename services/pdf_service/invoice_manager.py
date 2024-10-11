from services.pdf_service.invoice.our_company.domestic_invoice import DomesticInvoice
from services.pdf_service.invoice.our_company.foreign_invoice import ForeignInvoice
from services.pdf_service.invoice.other_company.domestic_invoice import OtherCompanyDomesticInvoice
from services.pdf_service.invoice.other_company.foreign_invoice import OtherCompanyForeignInvoice

class InvoiceManager:
    def __init__(self):
        self.invoices = []

    def process_invoices(self, data):
        # 여기서는 데이터에 따라 적절한 인보이스 클래스 호출
        if data['company'] == 'our_company':
            if data['type'] == 'domestic':
                invoice = DomesticInvoice(data)
            else:
                invoice = ForeignInvoice(data)
        else:
            if data['type'] == 'domestic':
                invoice = OtherCompanyDomesticInvoice(data)
            else:
                invoice = OtherCompanyForeignInvoice(data)

        self.invoices.append(invoice)
        return self.invoices
