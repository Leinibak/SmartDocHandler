import PyPDF2

class PDFReader:
    def extract_text(self, file):
        with open(file, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
        return text
