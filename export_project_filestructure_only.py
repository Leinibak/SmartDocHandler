import os

def should_include(path):
    # 제외할 디렉토리나 파일 패턴
    exclude_patterns = [
        '__pycache__',
        'venv',
        '.git',
        '.idea',
        '.vscode',
        '*.pyc',
        '*.pyo',
        '*.pyd',
        '*.db',
        '*.log'
    ]
    
    for pattern in exclude_patterns:
        if pattern in path:
            return False
    return True

def export_project_structure(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(root_dir):
            # 제외할 디렉토리 필터링
            dirs[:] = [d for d in dirs if should_include(os.path.join(root, d))]
            
            level = root.replace(root_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f'{indent}{os.path.basename(root)}/\n')
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                if should_include(file):
                    f.write(f'{sub_indent}{file}\n')

# 프로젝트 루트 디렉토리 경로 설정
root_directory = "C:/Users/debak/Dev/SmartDocHandler"
# 출력 파일 경로 설정
output_file = "C:/Users/debak/Dev/SmartDocHandler/project_structure.txt"

export_project_structure(root_directory, output_file)
print(f"Project structure exported to {output_file}")