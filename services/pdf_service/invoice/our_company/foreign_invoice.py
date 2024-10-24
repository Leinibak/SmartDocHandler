class ForeignInvoice:
    def __init__(self, data):
        self.data = data

    def extract(self):
        # 해외 인보이스에서 필요한 데이터 추출
        return {
            'invoice_number': self.data.get('invoice_number'),
            'date': self.data.get('date'),
            'total_amount': self.data.get('total_amount'),
            'currency': self.data.get('currency')
        }
