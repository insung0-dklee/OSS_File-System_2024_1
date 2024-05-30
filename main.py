import os
import shutil
import datetime
from fpdf import FPDF


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
        print("기능 3 실행.")
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


"""
파일 속성 출력 로직
@Param    
    filepath : 파일 경로

@Return
    없음
"""

def ViewFileAttribute(filepath):
    if os.path.exists(filepath):
        file_stats = os.stat(filepath)
        print(f"file destination : {filepath}")
        print(f"file size : {file_stats.st_size} 바이트")
        
        last_mod_time = datetime.datetime.fromtimestamp(file_stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        print(f"last edit time : {last_mod_time}")

        creation_time = datetime.datetime.fromtimestamp(file_stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        print(f"create time : {creation_time}")
    else:
        print(f"{filepath} 파일이 없습니다.")


"""
txt 파일을 PDF로 변환
(한글 지원x | 숫자와 영어만 가능)
cmd에서 "pip install cryptography"
위 " " 안의 명령어를 입력 후 엔터(라이브러리 설치)
위 과정을 거쳐 라이브러리를 설치해야 사용 가능함.

@Param  
    txt_path : txt 파일 경로
    pdf_path : 생성될 PDF 파일 경로

@Return
    없음
"""

def Conver_Txt_to_Pdf(txt_path, pdf_path):
    try:
        if not os.path.exists(txt_path):
            print(f"{txt_path} 파일이 없습니다.")
            return

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=14)
        with open(txt_path, 'r', encoding='utf-8') as file:
            for line in file:
                pdf.cell(200, 20, txt=line, ln=True)
        pdf.output(pdf_path)
        print(f"{pdf_path}로 Pdf 변환이 성공했습니다.")
    except Exception as e:
        print(f"Pdf 변환 중 오류 발생 => {e}")

"""
Using Example(아래 처럼 사용시 py파일과 같은 위치에 있어야함)

ViewFileAttribute("test.txt")
Conver_Txt_to_Pdf("test.txt", "output.pdf")
"""

