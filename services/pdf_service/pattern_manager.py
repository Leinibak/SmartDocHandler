import re

class PatternManager:
    def __init__(self):
        # 패턴을 client, doc_type, region으로 구분하여 저장
        self.patterns = {
            "debak": {
                "invoice": {
                    "domestic": r"\bInvoice Number: (\d+)\b",
                    "Foreign": r"\bForeign Invoice No: (\d+)\b"
                }
            },
            "another_company": {
                "Invoice": {
                    "Domestic": r"\bLocal Invoice No: (\d+)\b",
                    "Foreign": r"\bIntl Invoice No: (\d+)\b"
                }
            }
            # 필요한 만큼 더 많은 client, doc_type, region 패턴 추가 가능
        }

    def get_pattern(self, client, doc_type, region):
        """
        주어진 client, doc_type, region에 대한 패턴을 반환합니다.
        패턴이 없을 경우 None을 반환합니다.
        """
        # 반환되는 패턴이 딕셔너리인지 확인
        # return self.patterns.get(client.lower(), {}).get(doc_type.lower(), {}).get(region.lower(), {})
        return { "domestic": r"\bInvoice Number: (\d+)\b"}

    def extract_data(self, text, pattern):
        """
        주어진 텍스트에서 패턴을 사용해 데이터를 추출합니다.
        :param text: PDF에서 추출한 텍스트
        :param pattern: 사용할 정규 표현식 패턴
        :return: 추출된 데이터
        """
        if pattern:
            match = re.search(pattern, text)
            if match:
                print("Match:",match)
                return match.group(1)
        return None
