'''
파일 편집 패키지 (vim 생각하면 편합니다.)

현재 구현 상태
1. 파일 읽기
2. 파일 쓰기
3. 파일 내용 추가
4. 파일 내용 부분 삭제
5. 파일 내용 전체 삭제
'''

def file_edit():
    finish = False
    while not finish:
        
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print(" '읽기'      입력시 해당 파일의 내용을 출력")
            print(" '파일 생성 및 쓰기'  입력시 파일을 생성하고 원하는 내용을 작성")
            print(" '파일 내용 추가'  입력시 이미 생성된 파일에 원하는 내용을 추가 작성")
            print(" '파일 내용 부분 삭제'  입력시 이미 생성된 파일의 내용을 확인하고 원하는 부분을 삭제")
            print(" '파일 내용 전체 삭제'  입력시 이미 생성된 파일의 내용 전체를 삭제")
            print(" '종료'      입력시 프로그램을 종료할 수 있습니다.")
        elif select == "읽기":
            read_file()
        elif select == "파일 생성 및 쓰기":
            append_to_file()
        elif select == "파일 내용 추가":
            create_and_write_file()
        elif select == "파일 내용 부분 삭제":
            delete_partial_content()
        elif select == "파일 내용 전체 삭제":
            delete_file_content()
        elif select == '종료':
            print('파일 편집 기능을 종료합니다.')
            finish = True
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")


def read_file():
    """
    이미 생성된 파일을 읽어옴
    """
    file_path = input("읽고 싶은 파일의 경로를 입력하세요. : ")
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def create_and_write_file():
    """
    새 파일을 생성하고 원하는 내용을 기재
    """
    file_path = input("파일을 생성하고 싶은 디렉토리의 경로를 입력하세요. : ")
    content = input("쓰고 싶은 문장을 입력하세요. : ")
    with open(file_path, 'w') as file:
        file.write(content)

def append_to_file():
    """
    이미 생성된 파일에 원하는 내용을 추가 기재
    """
    file_path = input("내용을 추가할 파일의 경로를 입력하세요. : ")
    content = input("추가할 내용을 입력하세요. : ")
    with open(file_path, 'a') as file:
        file.write(content)

def delete_partial_content():
    """
    사용자에게 파일 내용을 보여줌
    삭제할 내용을 입력받은 뒤 해당 내용을 삭제한 새 내용을 파일에 기재
    """
    file_path = input("내용을 부분적으로 삭제할 파일의 경로를 입력하세요. : ")
    with open(file_path, 'r') as file:
        content = file.read()
    to_delete = input("삭제할 내용을 입력하세요. : ")
    new_content = content.replace(to_delete, '')
    with open(file_path, 'w') as file:
        file.write(new_content)

def delete_file_content():
    """
    이미 생성된 파일 안의 내용을 전체 삭제
    """
    file_path = input("전체 내용을 삭제할 파일의 경로를 입력하세요. : ")
    with open(file_path, 'w') as file:
        pass