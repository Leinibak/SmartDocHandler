from services.pdf_service.pattern_manager import PatternManager
import fitz  # PyMuPDF의 이름

class PDFProcessor:
    def __init__(self):
        self.pattern_manager = PatternManager()

    def process_pdf(self, file_path, patterns):
        # 파일에서 텍스트 추출 (예시)
        text = self._read_pdf(file_path)
        print("Text:", text)

        # PatternManager에서 패턴을 활용해 데이터 추출
        extracted_data = {}
        
        # patterns가 빈 딕셔너리인지 확인
        if patterns:
            for field, pattern in patterns.items():
                extracted_data[field] = self.pattern_manager.extract_data(text, pattern)

        return extracted_data

    def _read_pdf(self, file_path):
        """
        PDF 파일에서 모든 텍스트를 추출하여 문자열로 반환합니다.
        """
        # PDF 파일 열기
        doc = fitz.open(file_path)
        text = ""

        # 각 페이지의 텍스트 추출
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)  # 페이지 로드
            text += page.get_text("text")  # 텍스트 가져오기

        doc.close()  # 파일 닫기
        return text
