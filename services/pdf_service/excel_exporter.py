import os
import pandas as pd

class ExcelExporter:
    def export_to_excel(self, invoices, output_file):
        data = [invoice for invoice in invoices]
        df = pd.DataFrame(data)

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


# import pandas as pd

# class ExcelExporter:
#     def export_to_excel(self, invoices, output_file):
#         if not invoices:
#             print("No data to export. Excel file will not be created.")
#             return  # 데이터가 없으면 아무것도 하지 않음

#         data = [invoice.extract() for invoice in invoices]
#         df = pd.DataFrame(data)
        
#         # DataFrame이 비어있지 않은 경우에만 Excel 파일을 저장
#         if not df.empty:
#             df.to_excel(output_file, index=False)
#             print(f"Invoices successfully exported to {output_file}")
#         else:
#             print("DataFrame is empty. No file saved.")
