from smart_doc_handler.services.pdf_service.invoice.base_invoice import BaseInvoice

import re

class DomesticInvoice(BaseInvoice):
    def extract_data(self):
        invoice_number = self.extract_invoice_number()
        total_amount = self.extract_total_amount()
        return {
            'invoice_number': invoice_number,
            'total_amount': total_amount
        }

    def extract_invoice_number(self):
        match = re.search(r'Invoice Number:\s*(\d+)', self.text)
        if match:
            return match.group(1)
        return None

    def extract_total_amount(self):
        match = re.search(r'Total Amount:\s*([\d,.]+)', self.text)
        if match:
            return match.group(1)
        return None
