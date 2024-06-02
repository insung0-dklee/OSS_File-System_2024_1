from Control import Bookmark, FileEdit, FileControl, Duplicates, Readable

b_is_exit = False
version = "1.0.0"
bookmark_list = []

print(f"프로그램 버전: {version}")

while not b_is_exit:

    func = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")
    
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