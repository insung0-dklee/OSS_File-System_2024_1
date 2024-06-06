'''
파일 편집 패키지 (vim 생각하면 편합니다.)

현재 구현 상태
1. 파일 읽기
2. 파일 쓰기
3. 파일 단어 찾아 바꾸기
4. 파일 내용 복사 및 붙여넣기
'''

import os


def file_edit():
    finish = False
    while not finish:
        
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print(" '읽기'              입력시 해당 파일의 내용을 출력")
            print(" '파일생성'          입력시 파일을 생성하고 원하는 내용을 작성")
            print(" '찾아 바꾸기'       입력시 파일을 불러오고 원하는 단어를 찾아 새 단어로 바꿀 수 있습니다")
            print(" '복사 및 붙여넣기'  입력시 파일을 불러오고 원하는 부분을 찾아 다른 파일에 붙여넣을 수 있습니다")
            print(" '종료'             입력시 프로그램을 종료할 수 있습니다.")
        elif select == "읽기":
            read_file()
        elif select == "파일 생성 및 쓰기":
            create_and_write_file()
        elif select == "찾아 바꾸기":
            modify_file()
        elif select == "복사 및 붙여넣기":
            copy_and_paste_text()
        elif select == '종료':
            print('파일 편집 기능을 종료합니다.')
            finish = True
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")


def read_file():
    file_path = input("읽고 싶은 파일의 경로를 입력하세요. : ")
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def create_and_write_file():
    file_path = input("파일을 생성하고 싶은 디렉토리의 경로를 입력하세요. : ")
    content = input("쓰고 싶은 문장을 입력하세요. : ")
    with open(file_path, 'w') as file:
        file.write(content)

def modify_file():
    """
    이미 만들어진 파일의 내용을 읽고, 특정 문자열을 찾아 새 문자열로 바꿔주는 함수
    """
    file_path = input("찾아 바꾸기를 하고 싶은 파일의 경로를 입력하세요. : ")
    with open(file_path, 'r') as file:
        content = file.read()
    print(f"현재 파일 내용:\n{content}")
    old_string = input("찾을 단어를 입력하세요: ")
    new_string = input("바꿀 단어를 입력하세요: ")
    modified_content = content.replace(old_string, new_string)
    with open(file_path, 'w') as file:
        file.write(modified_content)
    print("찾아 바꾸기가 완료되었습니다.")

def copy_and_paste_text():
    """
    이미 만들어진 파일의 내용 중 일부를 복사하여 다른 파일에 붙여넣는 함수
    """
    source_file_path = input("복사할 내용이 있는 파일의 경로를 입력하세요: ")
    with open(source_file_path, 'r') as file:
        content = file.read()
    print(f"원본 파일 내용:\n{content}")
    start_index = int(input("복사할 부분의 시작 인덱스를 입력하세요(인덱스 0부터 시작) : "))
    end_index = int(input("복사할 부분의 끝 인덱스를 입력하세요 : "))
    text_to_copy = content[start_index:end_index+1]
    target_file_path = input("붙여넣을 파일의 경로를 입력하세요: ")
    with open(target_file_path, 'a') as file:
        file.write(text_to_copy)
    print("복사 및 붙여넣기가 완료되었습니다.")

def count_word():
    """
    이미 만들어진 파일 내에서 특정 단어가 몇 번 나오는지를 세주는 함수
    """
    file_path = input("단어 수 세기 기능을 사용하고 싶은 파일의 경로를 입력하세요: ")
    word = input("횟수를 셀 단어를 입력하세요: ")
    with open(file_path, 'r') as file:
        content = file.read()
    word_count = content.count(word)
    print(f"{word}는 {word_count}번 나옵니다.")


def combine_files(zip_path, jpg_path, output_path=None):
    """
    zip 파일과 jpg 파일을 이진 모드로 읽어서 결합하여 사진 파일을 생성합니다.
    생성된 사진 파일의 확장자를 zip으로 바꾸면 zip으로도 실행 가능합니다.
    단, JPEG 비트열을 앞에서부터 해석하는 알집이나 윈도우 기본 파일에서는 포맷이 에러 처리됩니다.
        winrar나 반디집 등의 프로그램으로 동작해야합니다.
    @Param
        zip_path : 압축 파일의 경로
        jpg_path : 사진 파일의 경로
        output_path : 저장할 폴더의 경로 (없으면 압축파일 경로 사용)
    @Return
        성공 시 True, 아니면 False
    @Example
        combine_files(zip_path, jpg_path, output_path)
    """
    # 입력된 경로가 존재하는지 확인
    if not os.path.exists(zip_path) or not os.path.exists(jpg_path):
        print("파일이 존재하지 않습니다.")
        return False
    
    # 입력된 경로가 파일인지 확인
    if not os.path.isfile(zip_path) or not os.path.isfile(jpg_path):
        print("파일이 아니거나 경로가 잘못되었습니다.")
        return False

    try:
        # 첫 번째 파일이 zip 파일인지 확인
        if os.path.splitext(zip_path)[1].lower() != '.zip':
            print("첫 번째 파일이 zip 파일이 아닙니다.")
            return False
        
        # 두 번째 파일이 jpg 파일인지 확인
        if os.path.splitext(jpg_path)[1].lower() != '.jpg':
            print("두 번째 파일이 jpg 파일이 아닙니다.")
            return False

        # 첫 번째 파일 열기 및 내용 읽기
        with open(zip_path, 'rb') as zip:
            zip_content = zip.read()
        
        # 두 번째 파일 열기 및 내용 읽기
        with open(jpg_path, 'rb') as jpg:
            jpg_content = jpg.read()
        
        # 두 파일의 내용을 결합하여 새로운 파일 생성
        combined_content = zip_content + jpg_content
        print("새로운 파일을 생성합니다.")
        # 새로운 파일 생성
        if output_path is None or not os.path.isdir(output_path):
            file_path = os.path.join(os.path.dirname(zip_path), f"{os.path.basename(zip_path)}_converted.jpg")
        else:
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            file_path = os.path.join(output_path, f"{os.path.basename(zip_path)}_converted.jpg")
        
        with open(file_path, 'wb') as output_file:
            output_file.write(combined_content)
        
        print(f"{output_path}에 파일을 생성했습니다.")
        return True
    
    except Exception as e:
        print(f"에러가 발생했습니다: {e}")
        return False

# 사용 예시
zip_path = r"C:\Users\user\Documents\카카오톡 받은 파일\HoloCure0629.zip"
jpg_path = r"C:\Users\user\Documents\카카오톡 받은 파일\KakaoTalk_20220131_115947269.jpg"
output_path = r"C:\Users\user\Documents\카카오톡 받은 파일\HoloCure0629_converted.jpg"
combine_files(zip_path, jpg_path, output_path)