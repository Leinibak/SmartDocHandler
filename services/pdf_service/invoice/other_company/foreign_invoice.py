class OtherCompanyForeignInvoice:
    def __init__(self, data):
        self.data = data

    def extract(self):
        # 다른 회사의 해외 인보이스 데이터 추출
        return {
            'invoice_number': self.data.get('invoice_number'),
            'date': self.data.get('date'),
            'total_amount': self.data.get('total_amount'),
            'currency': self.data.get('currency')
        }
