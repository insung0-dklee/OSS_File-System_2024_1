'''
파일 편집 패키지 (vim 생각하면 편합니다.)

현재 구현 상태
1. 파일 읽기
2. 파일 쓰기
'''

from os.path import isfile  # 파일 유효성 체크 모듈
from os.path import isdir   # 디렉토리 유효성 체크 모듈
'''
print(isfile(r'D:\test.txt')) # 참 : True , 없으면 : False
print(isdir(r'D:\test')) # 참 : True , 없으면 : False
'''

def file_edit():
    finish = False
    while not finish:
        
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print(" '읽기'      입력시 해당 파일의 내용을 출력")
            print(" '파일 생성 및 쓰기'  입력시 파일을 생성하고 원하는 내용을 작성")
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
    try:
        file_path = input("읽고 싶은 파일의 경로를 입력하세요. : ")
        with open(file_path, 'r') as file:
                content = file.read()
        if file_path.endswith('.txt'):
            return print(content)
        else :
            return content
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
    except PermissionError:
        print(f"파일을 읽을 권한이 없습니다: {file_path}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")


def create_and_write_file():
    try:
        file_path = input("파일을 생성하고 싶은 디렉토리 경로를 입력하세요. : ")

        with open(file_path, 'w') as file:
            content = input("쓰고 싶은 문장을 입력하세요. : ")
            file.write(content)
        print("파일이 성공적으로 생성되고 쓰기가 완료되었습니다.")
    except IsADirectoryError as e:
        print(f"디렉토리를 입력하셨습니다: {e}")
    except FileNotFoundError:
        print(f"지정된 디렉토리를 찾을 수 없습니다: {file_path}")
    except PermissionError:
        print(f"지정된 디렉토리에 대한 쓰기 권한이 없습니다: {file_path}")
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")