import os
import re

def search_files(directory, name_pattern, use_regex=False):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if use_regex:
                if re.match(name_pattern, file):
                    found_files.append(os.path.join(root, file))
            else:
                if file == name_pattern:
                    found_files.append(os.path.join(root, file))
    return found_files