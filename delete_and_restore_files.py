import os
import send2trash

def delete_file(path):
    try:
        send2trash.send2trash(path)
        print(f"File {path} sent to trash")
    except Exception as e:
        print(f"Error deleting file: {e}")

def restore_file_from_trash(trash_path, restore_path):
    try:
        if os.path.exists(trash_path):
            shutil.move(trash_path, restore_path)
            print(f"File restored from {trash_path} to {restore_path}")
        else:
            print(f"Trash file {trash_path} not found")
    except Exception as e:
        print(f"Error restoring file: {e}")
