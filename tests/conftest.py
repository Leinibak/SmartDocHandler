# tests/conftest.py

import pytest
import os

@pytest.fixture
def sample_pdf_path():
    # 샘플 PDF 파일의 경로를 반환합니다.
    # 실제 테스트에 사용할 샘플 PDF 파일을 'tests/sample_files/' 폴더에 두는 것을 권장합니다.
    return os.path.join(os.path.dirname(__file__), 'sample_files', 'domestic_invoice.pdf')

@pytest.fixture
def sample_text():
    # 샘플 텍스트 데이터를 반환합니다.
    return "Invoice Number: 123456\nTotal Amount: 1000.00"