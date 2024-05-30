from cryptography.fernet import Fernet
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
cryptography 라이브러리 설치필요

1.cmd 실행
2."pip install cryptography" 입력 후 엔터
 
"""

def Encrypt_Decrypt(file_name):

    sel = input("1.암호키 생성(최초1회) 2.암호화 3.복호화 : ")

    if sel == "1" :
        key = Fernet.generate_key()
        with open("encoding.key", "wb") as key_file:
            key_file.write(key)
        print(f"암호화 키를 생성했습니다.")

    elif sel == "2" :
        
        # 키 불러오기
        with open("encoding.key", "rb") as key_file:
            key = key_file.read()
        fernet = Fernet(key)
    
        # 파일 Read
        with open(file_name, "rb") as file:
            data = file.read()
        
        # 파일 Data Encoding(암호화)
        encryptedData = fernet.encrypt(data)
    
        # 암호화된 데이터를 파일에 저장(쓰기)
        with open(file_name, "wb") as file:
            file.write(encryptedData)
        
        print(f"{file_name}을 암호화 했습니다.")

    elif sel == "3" :

        # 키 불러오기
        with open("encoding.key", "rb") as key_file:
            key = key_file.read()
        fernet = Fernet(key)
    
        # 암호화된 파일 읽기
        with open(file_name, "rb") as file:
            encryptedData = file.read()
        
        # 암호화된 데이터 복호화
        decryptedData = fernet.decrypt(encryptedData)
    
       # 복호화된 데이터를 파일에 쓰기
        with open(file_name, "wb") as file:
            file.write(decryptedData)

        print(f"{file_name}을 복호화 했습니다.")

        

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

    elif func == "암호화 설정" :
        file_name = input("대상 경로를 입력하세요 : " )
        Encrypt_Decrypt(file_name)

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
