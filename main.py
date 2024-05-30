import os

def getParentDir(path):
    return os.path.dirname(path)

def delete_file(file_path):
    """
    지정된 파일 경로의 파일을 삭제하는 함수
    
    Args:
        file_path (str): 삭제할 파일의 경로
        
    Returns:
        str: 파일 삭제 결과 메시지
    """
    if os.path.exists(file_path):
        os.remove(file_path)
        return f"{file_path} 파일이 삭제되었습니다."
    else:
        return f"{file_path} 파일이 존재하지 않습니다."

