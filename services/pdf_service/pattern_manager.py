class PatternManager:
    def __init__(self):
        # 패턴 목록 또는 데이터베이스에서 패턴을 불러올 수 있습니다.
        self.patterns = {
            "domestic_invoice": r"\bInvoice Number: (\d+)\b",
            "foreign_invoice": r"\bForeign Invoice No: (\d+)\b",
            # 더 많은 패턴 추가 가능
        }

    def get_pattern(self, document_type):
        """
        주어진 문서 유형에 대한 패턴을 반환합니다.
        :param document_type: 'domestic_invoice', 'foreign_invoice' 등의 문자열
        :return: 해당 문서 유형에 대한 정규 표현식 패턴
        """
        return self.patterns.get(document_type, None)

    def extract_data(self, text, document_type):
        """
        주어진 텍스트에서 패턴을 사용해 데이터를 추출합니다.
        :param text: PDF에서 추출한 텍스트
        :param document_type: 문서 유형
        :return: 추출된 데이터
        """
        import re
        pattern = self.get_pattern(document_type)
        if pattern:
            match = re.search(pattern, text)
            if match:
                return match.group(1)
        return None
