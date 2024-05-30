
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


'''

    Read or Write txt file.
    @Param
        txt_path    :  Variables representing the path of the text
    @return
        None
    
    When use open(filename,mode)
    Mode has 4 types.
    r - read only
    w - write only(overlay)
    a - write only(add)
    x - write only(error if present file)
    
'''

def readOrWrite(txt_path):
    try:
        while True:
            RoW = input("1: 읽기 모드, 2: 쓰기 모드(덮어쓰기), 3:쓰기 모드(덧붙이기). 4: 종료 : ")

            if RoW == "1":
                with open(txt_path, "r") as file:
                    text = file.read()
                    print(text)

            elif RoW == "2":
                with open(txt_path, "w") as file:
                    text = input("적을 내용을 입력해주세요 : ")
                    file.write(text)

            elif RoW == "3":
                with open(txt_path, "a") as file:
                    text = input("적을 내용을 입력해주세요 : ")
                    file.write(text)

            elif RoW == "4":
                print("텍스트 읽기 및 쓰기를 종료합니다.")
                break

            else:
                print("잘못된 입력입니다. 다시 입력해주세요")

    except Exception as e:
        print(f"텍스트 읽기 및 쓰기 중 오류가 발생했습니다: {e}")


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
        print("텍스트 읽기 및 쓰기 기능 실행")
        txt_path = input("읽거나 수정할 텍스트 경로를 입력해주세요 : ")
        readOrWrite(txt_path)

    elif func == "복사":
        src = input("복사할 파일의 경로를 입력하세요: ")
        dest = input("복사할 위치를 입력하세요: ")
        copyFile(src, dest)

    elif func == "?":
        print("도움말: 1, 2, 3(텍스트 읽기 및 쓰기)을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")