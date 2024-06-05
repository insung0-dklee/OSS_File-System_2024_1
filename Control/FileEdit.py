'''
파일 편집 패키지 (vim 생각하면 편합니다.)

현재 구현 상태
1. 파일 읽기
2. 파일 쓰기
3. 파일 단어 찾아 바꾸기
4. 파일 내용 복사 및 붙여넣기
5. 이미지 파일 변환 (PNG, JPG)
6. 문서 파일 변환(DOCX → PDF)
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
            print("'이미지변환'        입력시 이미지 파일 형식을 변환할 수 있습니다.")
            print("'문서변환'          입력시 문서 파일 형식을 변환할 수 있습니다.")
            print(" '종료'             입력시 프로그램을 종료할 수 있습니다.")
        elif select == "읽기":
            read_file()
        elif select == "파일 생성 및 쓰기":
            create_and_write_file()
        elif select == "찾아 바꾸기":
            modify_file()
        elif select == "복사 및 붙여넣기":
            copy_and_paste_text()
        elif select == "이미지변환":
            print("이미지 파일 형식 변환 기능 실행")
            convert_image_format()
        elif select == "문서변환":
            print("문서 파일 형식 변환 기능 실행")
            convert_document_format()
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

def convert_image_format():
    input_path = input("변환할 이미지 파일의 경로를 입력하세요: ")
    output_format = input("변환할 형식을 입력하세요 (예: PNG, JPG): ").upper()
    try:
        img = Image.open(input_path)
        output_path = os.path.splitext(input_path)[0] + f".{output_format.lower()}"
        img.save(output_path)
        print(f"이미지가 {output_format} 형식으로 변환되었습니다: {output_path}")
    except Exception as e:
        print(f"이미지 변환 중 오류 발생: {e}")

def convert_document_format():
    input_path = input("변환할 문서 파일의 경로를 입력하세요: ")
    output_format = input("변환할 형식을 입력하세요 (예: PDF): ").upper()
    try:
        if output_format == "PDF":
            if input_path.endswith(".docx"):
                doc = Document(input_path)
                output_path = os.path.splitext(input_path)[0] + ".pdf"
                pdfkit.from_string(doc.text, output_path)
                print(f"문서가 PDF 형식으로 변환되었습니다: {output_path}")
            else:
                print("현재 .docx 파일만 PDF로 변환할 수 있습니다.")
        else:
            print("지원하지 않는 문서 형식입니다.")
    except Exception as e:
        print(f"문서 변환 중 오류 발생: {e}")