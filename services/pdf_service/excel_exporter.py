import pandas as pd

class ExcelExporter:
    def export_to_excel(self, invoices):
        data = [invoice.extract() for invoice in invoices]
        df = pd.DataFrame(data)
        df.to_excel('invoices_output.xlsx', index=False)
        print("Invoices successfully exported to invoices_output.xlsx")
