'''
파일 편집 패키지 (vim 생각하면 편합니다.)

현재 구현 상태
1. 파일 읽기
2. 파일 쓰기
'''

def file_edit():
    finish = False
    while not finish:
        
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print(" '읽기'      입력시 해당 파일의 내용을 출력")
            print(" '파일생성'  입력시 파일을 생성하고 원하는 내용을 작성")
            print(" '종료'      입력시 프로그램을 종료할 수 있습니다.")
        elif select == "읽기":
            read_file()
        elif select == "파일 생성 및 쓰기":
            create_and_write_file()
        elif select == '종료':
            print('파일 편집 기능을 종료합니다.')
            finish = True
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")


def read_file():
    while True:
        file_path = input("읽고 싶은 파일의 경로를 입력하세요. : ")
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다. 올바른 경로를 입력하세요.")
        except IOError:
            print("파일을 열 수 없습니다. 다시 시도하세요.")
        except UnicodeDecodeError:  # 인코딩 관련 오류 처리
            print("파일을 읽을 수 없습니다. 다시 입력해주세요.")

def create_and_write_file():
    file_path = input("파일을 생성하고 싶은 디렉토리의 경로를 입력하세요. : ")
    content = input("쓰고 싶은 문장을 입력하세요. : ")
    with open(file_path, 'w') as file:
        file.write(content)