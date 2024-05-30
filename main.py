
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
        '''
        기능 3에 구현했습니다.
        파일이나 폴더를 다른 곳으로 이동시키는 기능입니다.
        place, new_place라는 변수로 각각의 경로를 받아서 new_place에 저장된
        경로로 이동시킵니다. 그러나 new_place로 받을 때 \\로 끝나지 않으면 
        옮기는 파일 또는 폴더명이 바뀌는 건 고칠 수 없었습니다.
        '''
        print("기능 3 파일 또는 폴더 이동 실행.")
        place = input("이동시킬 파일 또는 폴더 이름까지 포함해서 경로 입력: ")
        new_place = input("이동할 경로를 입력(경로 마지막에는 \\으로 끝내야 함.): ")
        if os.path.exists(place):
            shutil.move(place, new_place)
        else:
            print("파일이 존재하지 않아 이동시킬 수 없습니다.")
        # Add functionality for option 3 here

    elif func == "복사":
        src = input("복사할 파일의 경로를 입력하세요: ")
        dest = input("복사할 위치를 입력하세요: ")
        copyFile(src, dest)

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")