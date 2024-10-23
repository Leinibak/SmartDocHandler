from services.pdf_service.pdf_reader import PDFReader

class PDFProcessor:
    def __init__(self, client, doc_type, region):
        self.client = client
        self.doc_type = doc_type
        self.region = region

    def process_files(self, files, patterns):

        extracted_data = []
        for file in files:
            # text = self.pdf_reader.extract_text(file)
            data = self.extract_data(file, patterns)  # patterns 인자를 전달
            extracted_data.append(data)
        return extracted_data

    def extract_data(self, text, patterns):
        # 데이터 추출 로직을 여기에 추가합니다.
        # 예를 들어, 정규 표현식을 사용하여 patterns를 기반으로 데이터 추출
        pass
        return {}  # 추출된 데이터를 반환합니다.
