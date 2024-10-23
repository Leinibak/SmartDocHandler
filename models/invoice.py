# models/invoice.py
class Invoice:
    def __init__(self, id, company_name, amount):
        self.id = id
        self.company_name = company_name
        self.amount = amount

    def extract(self):
        return {
            'ID': self.id,
            'Company Name': self.company_name,
            'Amount': self.amount,
        }
