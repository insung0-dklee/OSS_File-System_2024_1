'''
가독성을 높이는 기능들의 패키지
'''

import os





"""
    입력한 경로의 디렉토리 내 파일 크기를 KB, MB처럼 사람이 읽기쉽게 변환하여 보여주는 함수
    매개변수 size_in_bytes: 바이트 단위의 파일 크기
    리턴값 str: 사람이 읽기 쉬운 형식으로 변환된 파일 크기
"""
def get_human_readable_size(size_in_bytes):

    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024

"""
    주어진 디렉토리의 파일 크기를 사람이 읽기 쉬운 형식으로 출력
    매개변수 directory: 디렉토리 경로
    파일 사이즈 출력
"""
def display_file_sizes(directory):
    try:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                size_in_bytes = os.path.getsize(file_path)
                human_readable_size = get_human_readable_size(size_in_bytes)
                print(f"{filename}: {human_readable_size}")
    except Exception as e:
        print(f"Error: {e}")