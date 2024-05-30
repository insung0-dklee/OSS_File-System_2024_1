import os
import shutil
import zipfile  # A library for handling ZIP archive files (docx, xlsx, pptx)
import olefile  # A library for reading OLE format files (doc, xls, ppt)

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")

"""
Identify the type of an office file based on its content.

@Param
filepath: The path to the file to be identified.
    
@Return
The type of the office file (DOC, PPT, XLS, DOCX, PPTX, XLSX, UNKNOWN).
"""
def identify_office_file(filepath):
    with open(filepath, 'rb') as file:
        ole_signature = file.read(8)
        if ole_signature == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
            with olefile.OleFileIO(filepath) as ole:
                if ole.exists('WordDocument'):
                    return "DOC"
                elif any(ole.exists(stream) for stream in ['PowerPoint Document', 'PP40']):
                    return "PPT"
                elif any(ole.exists(stream) for stream in ['Workbook', 'Book']):
                    return "XLS"
    
    with open(filepath, 'rb') as file:
        xml_signature = file.read(4)
        if xml_signature == b'\x50\x4B\x03\x04':
            try:
                with zipfile.ZipFile(filepath, 'r') as zip:
                    if 'word/document.xml' in zip.namelist():
                        return "DOCX"
                    elif 'ppt/presentation.xml' in zip.namelist():
                        return "PPTX"
                    elif 'xl/workbook.xml' in zip.namelist():
                        return "XLSX"
            except zipfile.BadZipFile:
                pass

    return "MS Office 파일이 아닌 UNKNOWN."

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

if __name__ == "__main__":
    b_is_exit = False

    while not b_is_exit:
        func = input("기능 입력 (? 입력시 도움말) : ")

        if func == "1":
            print("기능 1 실행.")
            renameFile()

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

        elif func == "문서확인":
            filepath = input("확인할 파일의 경로를 입력하세요: ")
            filetype = identify_office_file(filepath)
            print(f"파일 유형은 {filetype}입니다.")
        
        elif func == "?":
            print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '문서확인'을 입력하여 파일 유형을 확인하거나 '종료'를 입력하여 종료합니다.")

        elif func.lower() == "종료":
            b_is_exit = True
            print("프로그램을 종료합니다.")

        else:
            print("알 수 없는 입력입니다. 다시 시도해주세요.")
