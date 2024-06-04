from moviepy.editor import *

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

def video_to_audio(video_path, audio_format='mp3'):
    """
    동영상 형식의 파일을 입력받고, 음악 혹은 소리를 추출해 저장하는 함수
    @Param
        video_path : 동영상 파일의 경로입니다.
                     ['mp4', 'avi', 'mov', 'mkv', 'wmv'] 중 하나 사용
        audio_format : 저장할 파일의 확장자입니다. 기본 mp3
                       ['mp3', 'aac', 'm4a', 'wav', 'ogg'] 중 하나 사용
    @Return
        오류 발생 시 False, 아니면 None
    @Examples
        video_to_audio(file_path, ogg)
    """
    # 지원되는 오디오 형식 확인
    supported_audio_formats = ['mp3', 'aac', 'm4a', 'wav', 'ogg']
    
    if audio_format not in supported_audio_formats:
        print(f"Error: '{audio_format}'은(는) 지원되지 않는 오디오 형식입니다. {supported_audio_formats} 중 하나를 입력하세요.")
        return False
    
    # 동영상 파일 확장자 추출
    video_extension = video_path.split('.')[-1].lower()
    
    # 지원되는 동영상 형식인지 확인
    if video_extension not in ['mp4', 'avi', 'mov', 'mkv', 'wmv']:
        print("Error: 지원되지 않는 동영상 형식입니다. MP4, AVI, MOV, MKV, WMV 형식 중 하나를 입력하세요.")
        return False
    
    # 동영상 파일 로드
    try:
        video_clip = VideoFileClip(video_path)
    except Exception as e:
        print(f"Error: 동영상 파일 로드 중 오류 발생: {e}")
        return False
    
    # 동영상에서 오디오 추출
    audio_clip = video_clip.audio
    
    # 출력 오디오 파일 경로 정의
    audio_file_path = video_path.rsplit('.', 1)[0] + f'.{audio_format}'
    
    # 오디오를 파일로 저장
    try:
        audio_clip.write_audiofile(audio_file_path, codec=audio_format)
    except Exception as e:
        print(f"Error: 오디오 파일 저장 중 오류 발생: {e}")
        return False
    
    # 클립 닫기
    video_clip.close()
    audio_clip.close()

    print(f"동영상 '{video_path}'를 오디오 '{audio_file_path}'로 변환했습니다.")
