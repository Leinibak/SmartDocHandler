from services.pdf_service.pattern_manager import PatternManager

class PDFProcessor:
    def __init__(self, file_path, document_type):
        self.file_path = file_path
        self.document_type = document_type
        self.pattern_manager = PatternManager()

    def process(self):
        # 예시: PDF 파일을 읽고 텍스트를 추출
        with open(self.file_path, 'r') as file:
            text = file.read()

        # 패턴 매니저를 사용하여 데이터 추출
        extracted_data = self.pattern_manager.extract_data(text, self.document_type)
        print(f"Extracted data: {extracted_data}")
