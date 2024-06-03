import difflib

def find_directory_diff(directory1, directory2):
    dcmp = difflib.Differ()
    for line in difflib.unified_diff(directory1, directory2, fromfile='dir1', tofile='dir2', lineterm=''):
        print(line)
