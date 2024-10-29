import os
import pandas as pd

class ExcelExporter:
    def export_to_excel(self, invoices, output_file):
        # Check if invoices is a list of dictionaries
        if all(isinstance(invoice, dict) for invoice in invoices):
            # Extract keys and values to create a DataFrame
            data = []
            for invoice in invoices:
                # Create a row dictionary for the DataFrame
                row = {key: value for key, value in invoice.items()}
                data.append(row)
            
            df = pd.DataFrame(data)
        else:
            # Handle the case where invoices are in string format
            data = {invoice.split(": ")[0]: invoice.split(": ")[1] for invoice in invoices}
            df = pd.DataFrame(data.items(), columns=["Invoice Type", "Invoice Number"])
        

        # 절대 경로로 지정
        output_dir = os.path.join(os.getcwd(), 'invoices_output')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_file_path = os.path.join(output_dir, output_file)
        df.to_excel(output_file_path, index=False)

        # 디버깅 메시지 추가
        if os.path.exists(output_file_path):
            print(f"Invoices successfully exported to {output_file_path}")
        else:
            print("Error: File not created.")
