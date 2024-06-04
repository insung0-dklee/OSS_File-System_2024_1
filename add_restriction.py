import os
import shutil

class LimitedDirectory:
    def __init__(self, path, max_size_bytes):
        self.path = path
        self.max_size_bytes = max_size_bytes

    def get_current_size(self):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(self.path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def add_file(self, file_path):
        file_size = os.path.getsize(file_path)
        if self.get_current_size() + file_size > self.max_size_bytes:
            raise Exception(f"용량 제한 초과: {self.max_size_bytes} bytes")
        shutil.copy2(file_path, self.path)

    def remove_file(self, file_name):
        file_path = os.path.join(self.path, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)