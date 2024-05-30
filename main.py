import os

def getParentDir(path):
    return os.path.dirname(path)

"""
Rename the file at the given path to the new name.

This function takes the full path of an existing file and a new file name, and it renames
the file to the new name while keeping it in the same directory. The function returns the 
new full path of the renamed file.

@Param
current_path : 
    The current full path of the file. This should include the directory path and the file name.
    For example: '/path/to/your/file.txt'.
new_name : 
    The new name for the file. This should only be the file name, not the full path.
    For example: 'new_file_name.txt'.

@Variable
dir_path :
    The directory path of the current file. Extracted from the current_path.
    For example: '/path/to/your'.
new_path :
    The new full path for the file after renaming. Combines dir_path and new_name.
    For example: '/path/to/your/new_file_name.txt'.

@Return
    The new full path of the renamed file. This will include the original directory path
    combined with the new file name.
    For example: '/path/to/your/new_file_name.txt'.
"""
def renameFile(current_path, new_name):
    dir_path = getParentDir(current_path)
    new_path = os.path.join(dir_path, new_name)
    os.rename(current_path, new_path)
    return new_path

"""
Example usage
The variable current_file_path represents the current full path of the file that you want to rename.
The variable new_file_name represents the new name for the file (not the full path, just the file name).
"""
current_file_path = '/path/to/your/file.txt'
new_file_name = 'new_file_name.txt'

# Rename the file and print the new path
new_file_path = renameFile(current_file_path, new_file_name)
print(new_file_path)