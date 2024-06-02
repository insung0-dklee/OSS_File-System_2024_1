import os  # OS 모듈을 가져와 파일 시스템 작업을 수행
import re  # 정규 표현식(Regex) 모듈을 가져와 패턴 매칭을 수행

# 주어진 디렉터리에서 파일을 검색하는 함수
# directory: 검색을 시작할 디렉터리 경로
# name_pattern: 검색할 파일 이름 또는 정규 표현식 패턴
# use_regex: 정규 표현식 사용 여부를 나타내는 불리언 값 (기본값: False)
def search_files(directory, name_pattern, use_regex=False):
    found_files = []  # 검색된 파일 경로를 저장할 리스트
    for root, dirs, files in os.walk(directory):  # 디렉터리를 재귀적으로 순회
        for file in files:  # 현재 디렉터리의 각 파일에 대해
            if use_regex:  # 정규 표현식을 사용할 경우
                if re.match(name_pattern, file):  # 파일 이름이 정규 표현식 패턴과 일치하는지 확인
                    found_files.append(os.path.join(root, file))  # 일치하는 파일 경로를 리스트에 추가
            else:  # 정규 표현식을 사용하지 않을 경우
                if file == name_pattern:  # 파일 이름이 정확히 일치하는지 확인
                    found_files.append(os.path.join(root, file))  # 일치하는 파일 경로를 리스트에 추가
    return found_files  # 검색된 파일 경로 리스트 반환
