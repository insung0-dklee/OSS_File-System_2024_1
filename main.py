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

def addFile(file_path):
    try:
        with open(file_path, 'w') as f:
            f.write("")
        print(f"파일이 성공적으로 추가되었습니다: {file_path}")
    except Exception as e:
        print(f"파일 추가 중 오류가 발생했습니다: {e}")

def deleteFile(file_path):
    try:
        os.remove(file_path)
        print(f"파일이 성공적으로 삭제되었습니다: {file_path}")
    except Exception as e:
        print(f"파일 삭제 중 오류가 발생했습니다: {e}")

def createDirectory(dir_path):
    try:
        os.makedirs(dir_path, exist_ok=True)
        print(f"디렉토리가 성공적으로 생성되었습니다: {dir_path}")
    except Exception as e:
        print(f"디렉토리 생성 중 오류가 발생했습니다: {e}")

def deleteDirectory(dir_path):
    try:
        shutil.rmtree(dir_path)
        print(f"디렉토리가 성공적으로 삭제되었습니다: {dir_path}")
    except Exception as e:
        print(f"디렉토리 삭제 중 오류가 발생했습니다: {e}")
    
def moveFile(src, dest):
    try:
        shutil.move(src, dest)
        print(f"파일이 성공적으로 이동되었습니다: {dest}")
    except Exception as e:
        print(f"파일 이동 중 오류가 발생했습니다: {e}")

class FileManagement:
    @staticmethod
    def findFileInCurrentDirectory():
        """
        현재 작업 디렉토리에 있는 모든 파일을 찾습니다.
        """
        current_directory = os.getcwd()
        files_in_current_directory = os.listdir(current_directory)
        return files_in_current_directory
    
    @staticmethod
    def writeToFile(file_path, content):
        """
        파일에 내용을 추가합니다.
        """
        try:
            with open(file_path, 'a') as f:
                f.write(content)
            print(f"파일에 내용이 성공적으로 추가되었습니다: {file_path}")
        except Exception as e:
            print(f"파일에 내용 추가 중 오류가 발생했습니다: {e}")

b_is_exit = False

while not b_is_exit:
    func = input("기능 입력 (? 입력시 도움말) : ")

    if func == "1":
        print("실행 -> 파일 추가")
        file_path = input("추가할 파일의 경로를 입력하세요: ")
        addFile(file_path)

    elif func == "2":
        print("실행 -> 파일 삭제")
        file_path = input("삭제할 파일의 경로를 입력하세요: ")
        deleteFile(file_path)

    elif func == "3":
        print("기능 3 실행.")
        dir_path = input("생성할 디렉토리의 경로를 입력하세요: ")
        createDirectory(dir_path)

    elif func == "4":
        print("기능 4 실행.")
        dir_path = input("삭제할 디렉토리의 경로를 입력하세요: ")
        deleteDirectory(dir_path)
    
    elif func == "5":
        print("기능 5 실행.")
        src = input("이동할 파일의 경로를 입력하세요: ")
        dest = input("이동할 위치의 디렉토리 경로를 입력하세요: ")
        moveFile(src, dest)

    elif func == "6":
        print("기능 6 실행.")
        print("현재 디렉토리에 있는 모든 파일 찾기.")
        files  = FileManagement.findFileInCurrentDirectory()
        if files:
            print("현재 디렉토리에 있는 모든 파일:")
            for file in files:
                print(file)
        else:
            print("현재 디렉토리에 파일이 없습니다.")

    elif func == "7":
        print("기능 7 실행.")
        print("파일에 내용 작성.")
        file_path = input("내용을 작성할 파일의 경로를 입력하세요: ")
        content = input("작성할 내용을 입력하세요: ")
        FileManagement.writeToFile(file_path, content)

    # 이름 변경 시, 생성되어 있는 파일/디렉토리 이름과 동일하게 입력할 경우 에러 발생
    elif func == "8":
        print("기능 8 실행.")
        old_path = input("이름을 변경할 파일 또는 디렉토리의 경로를 입력하세요: ")
        new_name = input("새로운 이름을 입력하세요: ")
        try:
            os.rename(old_path, new_name)
            print(f"파일 또는 디렉토리 이름이 성공적으로 변경되었습니다.")
        except Exception as e:
            print(f"이름 변경 중 오류가 발생했습니다: {e}")

    elif func == "복사":
        src = input("복사할 파일의 경로를 입력하세요: ")
        dest = input("복사할 위치를 입력하세요: ")
        copyFile(src, dest)

    elif func == "?":
        print("도움말: 1, 2, 3, 4, 5을 입력하여 기능을 선택하거나 '복사' 입력하여 파일 복사, '종료' 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")