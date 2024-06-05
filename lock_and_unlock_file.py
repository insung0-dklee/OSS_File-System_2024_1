import fcntl

def lock_file(file_path):
    file = open(file_path, 'a')
    fcntl.flock(file, fcntl.LOCK_EX)
    return file

def unlock_file(file):
    fcntl.flock(file, fcntl.LOCK_UN)
    file.close()


