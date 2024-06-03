'''
가독성을 높이는 기능들의 패키지
'''

import os


def readable():

    finish = False

    while not finish:

        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print("도움말")
            print(" '단순변환'      입력시 bytes를 읽기 쉽게 변환해줍니다.")
            print(" '디렉토리 탐색' 입력시 해당 디렉토리의 파일들의 크기를 보기 좋게 표시합니다. ")
            print(" '종료'          입력시 프로그램을 종료할 수 있습니다.")

        elif select == '단순변환':
            path = input("파일 경로를 입력하세요.")
            print(get_human_readable_size(os.path.getsize(path)))

        elif select == '디렉토리 탐색':
            display_file_sizes()

        elif select == "종료":
            print("중복 관리를 종료합니다.")
            finish = True

        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")


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