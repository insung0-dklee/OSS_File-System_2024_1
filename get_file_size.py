import os

def get_directory_size(dir_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def get_file_size(file_path):
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    return 0
