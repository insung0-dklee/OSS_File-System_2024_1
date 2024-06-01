import os

def delete_files_by_extension(directory, extension, exclude_files=None):
    """
    Args:
        directory (str): 파일들을 검사할 디렉토리의 경로
        extension (str): 삭제할 파일의 확장자 (ex: '.txt')
        exclude_files (list): 삭제하지 않을 파일 이름 목록 (default값은 None)
    """
    if exclude_files is None:
        exclude_files = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # 파일이 지정된 확장자로 끝나는지 확인하고, 제외 파일 목록에 없는지 확인한다.
        if filename.endswith(extension) and filename not in exclude_files:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")

