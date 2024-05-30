
import os
import shutil

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")

"""

createFile은 지정된 경로에 새로운 파일을 생성하는 함수입니다.
파일이 생성될 디렉터리가 존재하지 않으면, 해당 디렉터리를 생성합니다.

매개변수: 
path(src): 생성할 파일의 경로

예외 처리:
파일 생성 중 오류가 발생하면 예외 메세지를 출력합니다.

"""

def createFile(path):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as file:
            file.write("") 
        print(f"파일이 성공적으로 생성되었습니다: {path}")
    except Exception as e:
        print(f"파일 생성 중 오류가 발생했습니다: {e}")

"""

changeFileExtension은 지정된 파일의 확장자를 변경하는 함수입니다.

매개변수:
src(str): 확장자를 변경할 파일의 경로
new_ext (str): 새로운 확장자 (예: '.txt', 'md')

예외:
파일이 존재하지 않으면 오류 메세지를 출력합니다.
유효한 확장자가 입력되지 않으면 오류 메세지를 출력합니다.
파일 확장자 변경 중 오류가 발생하면 예외 메시지를 출력합니다.

"""

def changeFileExtension(src, new_ext):
    if not os.path.isfile(src):
        print(f"오류: '{src}' 파일이 존재하지 않습니다.")
        return

    if not new_ext:
        print("오류: 유효한 확장자를 입력하세요.")
        return

    base = os.path.splitext(src)[0]
    new_name = f"{base}.{new_ext.lstrip('.')}"

    try:
        os.rename(src, new_name)
        print(f"파일 확장자가 성공적으로 변경되었습니다: {new_name}")
    except Exception as e:
        print(f"파일 확장자 변경 중 오류가 발생했습니다: {e}")

b_is_exit = False

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        print("기능 1 실행.")
        # Add functionality for option 1 here

    elif func == "2":
        print("기능 2 실행.")
        # Add functionality for option 2 here

    elif func == "3":
        print("기능 3 실행.")
        # Add functionality for option 3 here

    elif func == "복사":
        src = input("복사할 파일의 경로를 입력하세요: ")
        dest = input("복사할 위치를 입력하세요: ")
        copyFile(src, dest)

    elif func == "파일 생성":
        path = input("생성할 파일의 경로를 입력하세요: ")
        createFile(path)
    
    elif func == "확장자 변경":
        src = input("확장자를 변경할 파일의 경로를 입력하세요: ")
        new_ext = input("새로운 확장자를 입력하세요: ")
        changeFileExtension(src, new_ext)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")