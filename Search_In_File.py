import os
import shutil

def search_in_file(file_path, keyword):
    with open(file_path, 'r') as file:
        return [line for line in file if keyword in line]
