import os
import shutil
import random
import string
from captcha.image import ImageCaptcha
from PIL import Image

def getParentDir(path):
    return os.path.dirname(path)

def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"파일이 성공적으로 복사되었습니다: {dest}")
    except FileNotFoundError:
        print("오류: 파일을 찾을 수 없습니다.")
    except PermissionError:
        print("오류: 파일에 대한 권한이 없습니다.")
    except Exception as e:
        print(f"파일 복사 중 오류가 발생했습니다: {e}")

def generate_captcha():
    image = ImageCaptcha(width=280, height=90)
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    data = image.generate(captcha_text)
    image_file = "captcha.png"
    image.write(captcha_text, image_file)
    return captcha_text, image_file

def display_captcha(image_file):
    img = Image.open(image_file)
    img.show()

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

    elif func.lower() == "회원가입":
        captcha_text, image_file = generate_captcha()
        display_captcha(image_file)
        user_input = input("화면에 보이는 캡차를 입력하세요: ")
        if user_input == captcha_text:
            print("회원가입이 완료되었습니다.")
        else:
            print("캡차가 올바르지 않습니다. 다시 시도해주세요.")

    elif func == "?":
        print("도움말: 1, 2, 3을 입력하여 기능을 선택하거나 '복사'를 입력하여 파일을 복사하거나 '회원가입'을 입력하여 회원가입 또는 '종료'를 입력하여 종료합니다.")

    elif func.lower() == "종료":
        b_is_exit = True
        print("프로그램을 종료합니다.")

    else:
        print("알 수 없는 입력입니다. 다시 시도해주세요.")
