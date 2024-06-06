from PIL import Image
import os

import ffmpeg
'''
파일 편집 패키지 (vim 생각하면 편합니다.)

현재 구현 상태
1. 파일 읽기
2. 파일 쓰기
3. 파일 단어 찾아 바꾸기
4. 파일 내용 복사 및 붙여넣기
'''

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

def compress_image(quality, input_image_path, output_image_path=None):
    """
    이미지 파일의 경로를 입력받아 용량을 줄이는 코드
    @Param
        quality : 0~100 사이의 값, 값이 낮을수록 압축률 증가
        input_image_path : 이미지 파일의 경로
        output_image_path : 출력할 폴더의 경로 (폴더가 아니면 무시)
    @Return
        성공 시 True, 아니면 False
    @Example
        compress_image(70, input_path, output_path)
        compress_image(40, input_path)
    """
    # 입력된 경로가 존재하는지 확인
    if not os.path.exists(input_image_path):
        print("파일이 존재하지 않습니다.")
        return False
    
    # 입력된 경로가 파일인지 확인
    if not os.path.isfile(input_image_path):
        print("파일이 아니거나 경로가 잘못되었습니다.")
        return False

    # 이미지 파일 확장자인지 확인
    file_name, file_extension = os.path.splitext(os.path.basename(input_image_path))
    if file_extension.lower() not in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
        print("확장자가 정상적이지 않습니다.")
        return False

    try: # 이미지 파일 처리
        print("이미지 파일 처리를 시작합니다.")
        image = Image.open(input_image_path)
        
        # JPEG 포맷으로 저장하면서 품질(quality) 설정
        # 파일명의 확장자(file_extension)을 변경해서 확장자 설정
        # 디렉터리가 아니거나, 입력값이 없으면 기존 파일이 있는 폴더에 생성
        if output_image_path is None or not os.path.isdir(output_image_path):
            file_path = os.path.join(os.path.dirname(input_image_path), f"{file_name}_compressed{file_extension}")
        else:
            # 디렉토리가 없으면 디렉토리 생성
            if not os.path.exists(output_image_path):
                os.makedirs(output_image_path)
            file_path = os.path.join(output_image_path, f"{file_name}_compressed{file_extension}")
        
        # 결과 출력
        image.save(file_path, 'JPEG', quality=quality)
        print(f"{file_path}에 성공적으로 저장했습니다.")
        return True

    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다 : {e}")
        return False

def compress_video(input_video_path, output_video_path=None, video_bitrate='500k', audio_bitrate='128k'):
    """
    동영상 파일의 경로를 입력받아 용량을 줄이는 코드
    @Param
        input_video_path : 이미지 파일의 경로
        output_video_path : 출력할 폴더의 경로 (폴더가 아니면 무시)
        video_bitrate : 비디오 비트레이트, 초기값 500k, 값이 낮을수록 압축률 증가
        audio_bitrate : 오디오 비트레이트, 초기값 128k, 값이 낮을수록 압축률 증가
    @Return
        성공 시 True, 아니면 False
    @Example
        compress_video(input_path, output_path)
        compress_video(input_path)
        compress_video(input_path, output_path, '1000k')
    """
    # 입력된 경로가 존재하는지 확인
    if not os.path.exists(input_video_path):
        print("파일이 존재하지 않습니다.")
        return False
    
    # 입력된 경로가 파일인지 확인
    if not os.path.isfile(input_video_path):
        print("파일이 아니거나 경로가 잘못되었습니다.")
        return False

    # 이미지 파일 확장자인지 확인
    file_name, file_extension = os.path.splitext(os.path.basename(input_video_path))
    if file_extension.lower() not in ['.mp4', '.avi', '.mov', '.wmv', '.mkv']:
        print("확장자가 정상적이지 않습니다.")
        return False

    try: # 이미지 파일 처리
        print("이미지 파일 처리를 시작합니다.")

        # 디렉터리가 아니거나, 입력값이 없으면 기존 파일이 있는 폴더에 생성
        if output_video_path is None or not os.path.isdir(output_video_path):
            file_path = os.path.join(os.path.dirname(input_video_path), f"{file_name}_compressed{file_extension}")
        else:
            # 디렉토리가 없으면 디렉토리 생성
            if not os.path.exists(output_video_path):
                os.makedirs(output_video_path)
            file_path = os.path.join(output_video_path, f"{file_name}_compressed{file_extension}")
        
        # 결과 출력
        (
            ffmpeg
            .input(input_video_path)
            .output(file_path, video_bitrate=video_bitrate, audio_bitrate=audio_bitrate)
            .run()
        )
        print(f"{file_path}에 성공적으로 저장했습니다.")
        return True

    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다 : {e}")