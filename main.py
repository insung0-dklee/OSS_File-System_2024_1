import os
import shutil

"""
Moves a file from the source path to the destination path.

@Param
    source : The source file path.
    destination : The destination file path.

@Return
    None
@Raises
    Prints an error message if the operation fails.
"""
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print(f"Moved file from {source} to {destination}")
    except Exception as e:
        print(f"Error moving file: {e}")

"""
Creates a directory at the specified path.

@Param
    directory_path : The path where the new directory should be created.

@Return
    None
@Raises
    Prints an error message if the operation fails.
"""
def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Created directory {directory_path}")
    except Exception as e:
        print(f"Error creating directory: {e}")

"""
Lists all files in the specified directory.

@Param
    directory : The directory path to list files from.

@Return
    A list of filenames in the directory.
@Raises
    Prints an error message if the operation fails and returns an empty list.
"""
def list_files(directory):
    try:
        files = os.listdir(directory)
        print(f"Files in {directory}: {files}")
        return files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []

"""
Gets the parent directory of the specified path.

@Param
    path : The file or directory path.

@Return
    The parent directory path.
"""
def getParentDir(path):
    return os.path.dirname(path)

"""
Main function to provide a menu for file system operations.
Allows the user to move files, create directories, list files, and get the parent directory of a path.

@Return
    None
"""
def main():
    while True:
        print("\nFile System Operations:")
        print("1. Move File")
        print("2. Create Directory")
        print("3. List Files")
        print("4. Get Parent Directory")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            source = input("Enter the source file path: ")
            destination = input("Enter the destination path: ")
            move_file(source, destination)
        elif choice == '2':
            directory_path = input("Enter the directory path to create: ")
            create_directory(directory_path)
        elif choice == '3':
            directory = input("Enter the directory path: ")
            list_files(directory)
        elif choice == '4':
            path = input("Enter the file or directory path: ")
            parent_dir = getParentDir(path)
            print(f"Parent directory of {path} is {parent_dir}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
