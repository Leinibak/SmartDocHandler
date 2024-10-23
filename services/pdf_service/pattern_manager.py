class PatternManager:
    def __init__(self):
        # 패턴을 client, doc_type, region로 구분하여 저장
        self.patterns = {
            "debak": {
                "invoice": {
                    "domestic": r"\bInvoice Number: (\d+)\b",
                    "foreign": r"\bForeign Invoice No: (\d+)\b"
                }
            },
            "another_company": {
                "invoice": {
                    "domestic": r"\bLocal Invoice No: (\d+)\b",
                    "foreign": r"\bIntl Invoice No: (\d+)\b"
                }
            }
            # 필요한 만큼 더 많은 client, doc_type, region 패턴 추가 가능
        }

    def get_pattern(self, client, doc_type, region):
        """
        주어진 client, doc_type, region에 대한 패턴을 반환합니다.
        :param client: 고객 이름 (예: 'debak')
        :param doc_type: 문서 유형 (예: 'invoice')
        :param region: 지역 (예: 'domestic', 'foreign')
        :return: 해당 client, doc_type, region에 대한 정규 표현식 패턴
        """
        # 다중 수준 딕셔너리에서 값을 안전하게 가져옴
        return self.patterns.get(client, {}).get(doc_type, {}).get(region, None)

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
