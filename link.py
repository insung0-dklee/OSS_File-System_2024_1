import os

def create_symlink(target, link_name):
    os.symlink(target, link_name)

def is_symlink(path):
    return os.path.islink(path)

def create_hardlink(target, link_name):
    os.link(target, link_name)

def is_hardlink(path):
     """하드 링크 여부는 직접적으로 확인하기 어렵지만, os.stat()으로 inode 번호를 통해 확인 가능하다."""
    try:
        stat_info = os.stat(path)
        return stat_info.st_nlink > 1
    except FileNotFoundError:
        return False

