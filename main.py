def preview_file(file_path, num_lines=10):
    with open(file_path, 'r') as file:
        for i in range(num_lines):
            print(file.readline().strip())
