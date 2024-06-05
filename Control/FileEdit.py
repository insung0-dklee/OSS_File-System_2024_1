'''
파일 편집 패키지 (vim 생각하면 편합니다.)

현재 구현 상태
1. 파일 읽기
2. 파일 쓰기
3. 파일 단어 찾아 바꾸기
4. 파일 내용 복사 및 붙여넣기
'''
import string

def file_edit():
    finish = False
    while not finish:
        
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print(" '읽기'              입력시 해당 파일의 내용을 출력")
            print(" '파일생성'          입력시 파일을 생성하고 원하는 내용을 작성")
            print(" '찾아 바꾸기'       입력시 파일을 불러오고 원하는 단어를 찾아 새 단어로 바꿀 수 있습니다")
            print(" '복사 및 붙여넣기'  입력시 파일을 불러오고 원하는 부분을 찾아 다른 파일에 붙여넣을 수 있습니다")
            print(" '비밀번호 생성/해제'입력시 파일을 암호화하거나 복호화합니다.")
            print(" '종료'             입력시 프로그램을 종료할 수 있습니다.")
        elif select == "읽기":
            read_file()
        elif select == "파일 생성 및 쓰기":
            create_and_write_file()
        elif select == "찾아 바꾸기":
            modify_file()
        elif select == "복사 및 붙여넣기":
            copy_and_paste_text()
        elif select == "비밀번호 설정/해제":
            endecrypt()
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

def endecrypt():

    finish = False

    while not finish:
        file_path = input("비밀번호를 설정하거나 해제할 파일 경로를 입력하세요. : ")
        select = input("파일을 암호화하려면 '암호화', 복호화하려면 '복호화', 다른 메뉴에 접근하려면 '취소'를 입력하세요. : ")
        if select == '암호화':
            password = input("복호화 시 사용할 암호를 입력하세요. (알파벳 대문자/소문자와 숫자, 특수문자 조합) : ")
            with open(file_path, 'r') as file:
                content = file.read()
                newcontent = encrypt(content, password)
            with open(file_path, 'w') as file:
                file.write(newcontent)
            print("암호화 된 파일을 확인하세요.")
            finish = True

        elif select == '복호화':
            password = input("암호화 시 입력한 암호를 입력하세요. (알파벳 대문자/소문자와 숫자, 특수문자 조합) : ")
            with open(file_path, 'r') as file:
                content = file.read()
                pastcontent = decrypt(content, password)
                if (pastcontent == False):
                    print("잘못된 비밀번호입니다.")
                else:
                    with open(file_path, 'w') as file:
                        print("비밀번호가 맞습니다. 복호화 된 파일을 확인하세요.")
                        file.write(pastcontent)
                    finish = True

        elif select == '취소':
            print('파일 편집 기능을 종료합니다.')
            finish = True

        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")


"""
@functions:
    endycrypt: function that encrypts or decrypts a file with personal password.

@params
    (string) content: data in the file
    (string) password: user input
    (string) basekey: string used to make plates for crytogram

@explain
    Encrypt the content using the en_password from the user, hiding the password in the returned file.
    Decrypt the cryptogram using the de_password from the user.
    After the decryption, comparing the en_password and de_password. If they are same, return the original file.
"""
def encrypt(content, password):

    basekey = string.printable
    baselen = len(basekey)
    plate = len(password)
    plates = make_plates(password, basekey)
    index = []

    for i, key in enumerate(password):
        for id, char in enumerate(plates[i]):
           if key == char:
                index.append(id)
                break
           
    encontent = []
    pnum = 0
    content = password + content
    for char in content:
        enchar = plates[pnum][index[pnum]]
        encontent.append(enchar)
        for id, base in enumerate(plates[pnum]):
            if(base == char):
                char_id = id
        for p_id in range(len(index)):
            index[p_id] = (index[p_id] + char_id) % baselen
        pnum = (pnum + 1) % plate

    for i in index:
        encontent.append(' ')
        encontent.append(str(i))
    newcontent = ''.join(encontent)

    return newcontent


def decrypt(content, password):

    basekey = string.printable
    baselen = len(basekey)
    plate = len(password)
    plates = make_plates(password, basekey)
    index = []
    content = list(content)

    for i in range(plate * 4):
        num = []
        while content[-1] != ' ':
            num.append(content[-1])
            content.pop()
        content.pop()
        num = int(''.join(reversed(num)))
        index.append(num)
        if len(index) == plate:
            break
    index.reverse()

    pnum = (len(content) - plate) % plate - 1 #plate = len(password)
    decontent = []
    for i in range(len(content)):
        for id, base in enumerate(plates[pnum]):
            if(base == content[-(i + 1)]):
                preindex = id
        char_id = index[pnum] - preindex
        if char_id < 0:
            char_id += baselen
        for p_id in range(len(index)):
            index[p_id] = index[p_id] - char_id
            if index[p_id] < 0:
                index[p_id] += baselen
        dechar = plates[pnum][char_id]
        pnum -= 1
        if pnum < 0:
            pnum += plate
        decontent.append(dechar)
    decontent.reverse()
    depass = ''.join(decontent[:plate])

    if (depass == password):
        pastcontent = ''.join(decontent[plate:])
        return pastcontent
    else:
        return False

def make_plates(password, basekey):
    allplate = len(password)
    baselen = len(basekey)
    plates = []
    for plate in range(allplate):
        baseplate = []
        for i in range(plate + 1):
            for id in range(len(basekey)):
                if i + id * (plate + 1) > baselen - 1:
                    break
                baseplate.append(basekey[i + id * (plate + 1)])
        plates.append(baseplate)
    return plates


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
