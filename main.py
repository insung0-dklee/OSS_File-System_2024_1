import os

def getParentDir(path):
    return os.path.dirname(path)
def rename_file():
     files = os.listdir('.')
     print("현재 디렉토리의 파일 목록:")
     for idx, file in enumerate(files):
         print(f"{idx+1}. {file}")
     file_index = int(input("변경할 파일을 선택하세요 (번호 입력): ")) - 1
     old_filename = files[file_index]
     new_filename = input("새로운 파일 이름을 입력하세요: ")
     try:
         os.rename(old_filename, new_filename)
         print(f"'{old_filename}' 파일이 '{new_filename}'로 변경되었습니다.")
     except FileNotFoundError:
         print("파일을 찾을 수 없습니다.")
     except FileExistsError:
         print("동일한 이름의 파일이 이미 존재합니다.")
 
rename_file()
