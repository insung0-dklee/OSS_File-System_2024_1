import os
import re

def search_files(directory, name_pattern, use_regex=False):
    
    """
    주어진 디렉토리에서 파일을 검색하여 일치하는 파일의 경로 목록을 반환합니다.
    
        directory (str): 검색을 시작할 디렉토리 경로
        name_pattern (str 또는 정규식): 검색할 파일 이름 또는 정규식 패턴
        use_regex (bool, optional): 정규식 사용 여부를 지정하는 플래그. 기본값은 False입니다.
    
        list: 일치하는 파일의 절대 경로 목록
    """

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