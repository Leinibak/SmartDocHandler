from services.pdf_service.pdf_processor import PDFProcessor
from services.pdf_service.excel_exporter import ExcelExporter
from services.pdf_service.pattern_manager import PatternManager

class InvoiceManager:
    def __init__(self):
        self.pdf_processor = PDFProcessor()
        self.excel_exporter = ExcelExporter()
        self.pattern_manager = PatternManager()

    def process_invoices(self, client, doc_type, region, files):
        patterns = self.pattern_manager.get_patterns(client, doc_type, region)
        invoices = []

        for file in files:
            invoice_data = self.pdf_processor.process_pdf(file, patterns)
            invoices.append(invoice_data)

        output_file = self.excel_exporter.export_to_excel(invoices)
        return output_file
