
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
from Control import FileControl
from Control import Duplicates
from Control import Readable
# 파일 관리 시스템
# - 중복 파일 탐지 및 삭제: 주어진 디렉토리에서 중복 파일을 찾아내고, 중복된 파일을 삭제합니다.
# - 파일 이름 변경: 사용자가 지정한 파일의 이름을 변경합니다.
# - 파일 메타데이터 관리: 파일의 생성 시간, 수정 시간, 파일 크기를 출력합니다.

b_is_exit = False

while not b_is_exit:

    func = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")
    bookmark_list = []

    if func == "파일편집":
        print("파일 편집 기능 실행")
        FileEdit.file_edit()

    elif func == "즐겨찾기":
        print("즐겨찾기 기능 실행.")
        Bookmark.bookmark(bookmark_list)

    elif func == "파일관리":
        print("파일 관리 기능 실행")
        FileControl.file_control()

    elif func == "가독성":
        print("가독성 기능 실행")
        Readable.readable()

    elif func == "중복관리":
        print("중복 관리 기능 실행")
        Duplicates.duplicates()

    elif func == "?":
        print("""
                [도움말]
                '파일편집' 입력시 파일을 편집할 수 있습니다.
                '즐겨찾기' 입력시 즐겨찾기 기능을 사용할 수 있습니다.
                '파일관리' 입력시 파일을 관리할 수 있습니다.
                '가독성'   입력시 파일의 단위를 읽기 좋게 볼 수 있습니다.
                '중복관리' 입력시 중복 파일을 관리할 수 있습니다.
                '종료'     입력시 프로그램을 종료합니다.
            """)

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요. : ")

"""
파일이름 변경 함수 renameFile 설명

매개변수는 없음.

이름을 변경할 파일의 경로와 새로운 파일이름을 입력받음.

입력받은 파일경로의 부모 디렉토리를 getParentDir함수로 구해서 새로운 파일 경로를 생성함.
os.rename함수로 파일 이름을 변경함.

성공 시, 기존경로, 바뀐경로를 출력함.
실패 시, 에러 메시지 출력함.
"""
def renameFile():
    try:
        srcPath = input("이름을 변경할 파일의 경로 입력: ")
        newName = input("새로운 파일이름 입력: ")
        parentDir = getParentDir(srcPath)
        newPath = os.path.join(parentDir, newName)
        os.rename(srcPath, newPath)
        print("기존경로: ", srcPath, " 바뀐경로: ", newPath, " 변경완료!")
    except Exception as e:
        print("파일이름 변경 중 에러발생", e)


"""
기능을 선택할 수 있음

1 입력 시, 파일 이름 변경
0 입력 시, 프로그램 종료

잘못된 입력은 다시 입력하도록 함

추가기능 구현 시, 조건문 추가
"""
if __name__ == "__main__":
    while True:
        print("--------------------------------")
        print("기능 선택")
        print("--------------------------------")
        print("1. 파일이름 변경")
        print("0. 종료")

        select = input("입력 (0번 입력시, 종료): ")
        print("\n")


        if select == '1':
            renameFile()
            
        
        elif select == '0':
            print("종료")
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")
        
