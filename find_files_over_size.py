def find_files_over_size(directory, size):
    files = [(root, name)
             for root, _, files in os.walk(directory)
             for name in files
             if os.path.getsize(os.path.join(root, name)) > size]
    return files
