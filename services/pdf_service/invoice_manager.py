from services.pdf_service.pdf_processor import PDFProcessor
from services.pdf_service.excel_exporter import ExcelExporter
from services.pdf_service.pattern_manager import PatternManager

class InvoiceManager:
    def __init__(self):
        self.pdf_processor = PDFProcessor()
        self.excel_exporter = ExcelExporter()
        self.pattern_manager = PatternManager()

    def process_invoices(self, client, doc_type, region, files):
        patterns = self.pattern_manager.get_pattern(client, doc_type, region)
        
        # patterns의 내용을 확인
        print("Patterns:", patterns)  # patterns가 무엇인지 확인
        if not patterns:
            print("No patterns found for the given client, doc_type, and region.")
            return None

        invoices = []
        for file in files:
            invoice_data = self.pdf_processor.process_pdf(file, patterns)
            invoices.append(invoice_data)

        # output_file = self.excel_exporter.export_to_excel(invoices)

        output_file_name = f'{client}_{doc_type}_{region}_invoices.xlsx'  # Define the output filename
        self.excel_exporter.export_to_excel(invoices, output_file_name)  # Pass the output file name


        return output_file_name
        
