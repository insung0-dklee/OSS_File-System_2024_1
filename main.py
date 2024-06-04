import os
import ctypes

def is_hidden(file_path):
    # 파일의 속성을 확인하여 숨겨진 파일인지 여부를 판단하는 함수
    attribute = ctypes.windll.kernel32.GetFileAttributesW(file_path)
    return attribute & 0x2  # FILE_ATTRIBUTE_HIDDEN

def find_hidden_files(directory):
    # 주어진 디렉터리에서 숨겨진 파일을 찾아 리스트로 반환하는 함수
    hidden_files = []
    for root, dirs, files in os.walk(directory):
        for name in files + dirs:
            full_path = os.path.join(root, name)
            if is_hidden(full_path):
                hidden_files.append(full_path)
    return hidden_files

# 검색할 디렉터리 경로
directory = r"C:\\path\\to\\directory"  # 원하는 경로로 수정
hidden_files = find_hidden_files(directory)

# 찾은 숨겨진 파일 목록 출력
for file in hidden_files:
    print(file)