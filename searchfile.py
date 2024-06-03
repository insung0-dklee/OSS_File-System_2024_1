import os
import re

def search_files(directory, name_pattern, use_regex=False):
    # 검색된 파일의 경로를 저장할 리스트를 초기화합니다.
    found_files = []

    # os.walk를 사용하여 지정된 디렉토리와 모든 하위 디렉토리를 순회합니다.
    for root, dirs, files in os.walk(directory):
        # 현재 디렉토리의 파일들을 순회합니다.
        for file in files:
            if use_regex:
                # 정규 표현식을 사용하여 파일 이름을 매칭합니다.
                if re.match(name_pattern, file):
                    # 매칭된 파일의 전체 경로를 리스트에 추가합니다.
                    found_files.append(os.path.join(root, file))
            else:
                # 정규 표현식을 사용하지 않고 파일 이름을 직접 비교합니다.
                if file == name_pattern:
                    # 매칭된 파일의 전체 경로를 리스트에 추가합니다.
                    found_files.append(os.path.join(root, file))
    
    # 매칭된 파일들의 경로가 담긴 리스트를 반환합니다.
    return found_files