import os
root_directory_path = "c:/"

def export_folder_code(root_dir, folder_name, output_file):
    folder_path = os.path.join(root_dir, folder_name)
    
    if not os.path.exists(folder_path):
        print(f"{folder_name} folder not found at {folder_path}")
        return

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(('.py', '.js', '.jsx', '.ts', '.tsx', '.html', '.css')):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, folder_path)
                    
                    out_file.write(f"File: {relative_path}\n")
                    out_file.write("=" * (len(relative_path) + 6) + "\n\n")
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as in_file:
                            content = in_file.read()
                            out_file.write(content)
                    except Exception as e:
                        out_file.write(f"[Error reading file: {str(e)}]\n")
                    
                    out_file.write("\n\n" + "=" * 50 + "\n\n")

    print(f"{folder_name} folder code exported to {output_file}")

# 프로젝트 루트 디렉토리 경로 설정
root_directory = root_directory_path

# 처리할 폴더 목록
folders = ['api', 'frontend', 'models', 'services', 'tests', 'utils']

# 각 폴더에 대해 코드 추출 실행
for folder in folders:
    output_file = f"{root_directory_path}/{folder}_code.txt"
    export_folder_code(root_directory, folder, output_file)