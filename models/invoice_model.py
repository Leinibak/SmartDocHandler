class InvoiceModel:
    def __init__(self, invoice_number, total_amount):
        self.invoice_number = invoice_number
        self.total_amount = total_amount

    def to_dict(self):
        return {
            "invoice_number": self.invoice_number,
            "total_amount": self.total_amount
        }
