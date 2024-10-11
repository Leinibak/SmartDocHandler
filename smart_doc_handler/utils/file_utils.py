import os

def save_file(uploaded_file, save_path):
    uploaded_file.save(save_path)

def get_file_extension(filename):
    return os.path.splitext(filename)[1]
