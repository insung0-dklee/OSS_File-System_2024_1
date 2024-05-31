
"""
현재 경로에 특정 파일이나 디렉토리가 존재하는지를 확인하기 위해 import os를 사용
파일을 이동이나 복사하기 위해 shutil 모듈을 사용하였음
파일 탐색기에서의 잘라내기 기능을 구현함
cut_file 함수는 잘라낼 파일의 경로와 붙여넣을 경로를 매개변수로 함
이때 붙여넣을 경로에 입력이 잘못됐을 경우 에러를 발생시킴
b_is_exit 변수를 0으로 초기화하고
1을 입력하였을때 잘라내기 기능이 구현되도록 함수를 작성하였음
favorites : 즐겨찾기 목록
addFavorite() : 원하는 파일을 즐겨찾기에 추가하는 함수
showFavorites() : 즐겨찾기 안의 파일 목록을 순서대로 출력하는 함수
"""

from Control import Bookmark
from Control import FileEdit
# 파일 관리 시스템
# - 중복 파일 탐지 및 삭제: 주어진 디렉토리에서 중복 파일을 찾아내고, 중복된 파일을 삭제합니다.
# - 파일 이름 변경: 사용자가 지정한 파일의 이름을 변경합니다.
# - 파일 메타데이터 관리: 파일의 생성 시간, 수정 시간, 파일 크기를 출력합니다.

b_is_exit = False

while not b_is_exit:

    func = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")
    bookmark_list = []

    if func == "파일 편집":
        print("파일 편집 기능 실행")
        FileEdit.file_edit()

    elif func == "즐겨찾기":
        print("즐겨찾기 기능 실행.")
        Bookmark.bookmark(bookmark_list)
        # Add functionality for option 2 here

    elif func == "파일 관리":
        print("파일 관리 기능 실행")
        # Add functionality for option 3 here

    elif func == "가독성":
        print("가독성 기능 실행")

    elif func == "?":
        print("""
                [도움말]
                1 을 입력하여 잘라내기(이동)하거나
                '즐겨찾기' 입력시 즐겨찾기 기능 실행
                3을 입력하여 기능을 선택하거나 
                '복사' 입력시 파일을 복사하거나 
                '종료'를 입력하여 종료합니다.
            """)

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
