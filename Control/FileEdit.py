from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
import re, os

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

def convert_to_seconds(time_str):
    """
    시간 문자열을 초 단위로 변환합니다. 포맷: 시간:분:초
    @Param
        time_str : 포맷 시간
    """
    # 정규표현식으로 포맷 검사
    if not re.match(r'^\d{2}:\d{2}:\d{2}$', time_str):
        print("시간 형식이 잘못되었습니다. 올바른 형식: 시간:분:초 (예: 00:10:00)")
        return None
    
    parts = list(map(int, time_str.split(':')))
    return parts[0] * 3600 + parts[1] * 60 + parts[2]

def process_video(file_path, start_time, end_time, output_dir=None):
    """
    동영상 파일의 길이를 출력하고, 입력받은 시간 범위만큼 동영상을 잘라 저장합니다.
    시간은 각각 (시간:분:초) 단위로 입력합니다.
    저장할 폴더가 지정되지 않으면 기존 파일의 위치에 생성합니다.
    @Param
        file_path : 동영상 파일의 경로
        start_time : 시작 시간 (포맷: 시간:분:초)
        end_time : 종료 시간 (포맷: 시간:분:초)
        output_dir : 출력 동영상 파일을 저장할 폴더 경로 (기본값: None)
    @Return
        성공 시 True, 아니면 False
    @Example
        process_video(file_path, start_time, end_time, output_dir)
        process_video(file_path, start_time, end_time)
    """
    if not os.path.isfile(file_path):
        print("파일이 존재하지 않습니다.")
        return False
    
    try:
        # 동영상 불러오기
        video = VideoFileClip(file_path)
        video_duration = video.duration
        print(f"동영상 길이: {video_duration}초")
        
        # 시작 시간과 종료 시간을 초 단위로 변환
        start_seconds = convert_to_seconds(start_time)
        end_seconds = convert_to_seconds(end_time)

        if start_seconds is None or end_seconds is None:
            return False
        
        if start_seconds >= video_duration:
            print("시작 시간이 동영상 길이를 초과합니다.")
            return False
        
        if end_seconds > video_duration:
            print("종료 시간이 동영상 길이를 초과합니다.")
            return False

        if start_seconds >= end_seconds:
            print("시작 시간이 종료 시간보다 크거나 같습니다.")
            return False
        
        print("동영상 처리를 시작합니다.")
        # 동영상 자르기
        new_video = video.subclip(start_seconds, end_seconds)
        
        # 저장할 파일 경로 결정
        file_name, _ = os.path.splitext(os.path.basename(file_path))
        if output_dir:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_file_path = os.path.join(output_dir, f"{file_name}_clip.mp4")
        else:
            output_file_path = os.path.join(os.path.dirname(file_path), f"{file_name}_clip.mp4")
        
        # 동영상 저장
        new_video.write_videofile(output_file_path, codec="libx264", audio_codec="aac")
        print(f"잘라낸 동영상을 '{output_file_path}'로 저장했습니다.")
        return True

    except Exception as e:
        print(f"동영상 처리 중 오류 발생: {e}")
        return False

    finally:
        if 'video' in locals():
            video.reader.close()
            video.audio.reader.close_proc()