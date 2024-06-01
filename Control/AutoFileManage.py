# flake8: noqa
import json
import re
import os
import shutil
import time

"""
파일 자동 관리 코드
작성자: 권혁준
학번: 22311905
일자: 2024-06-01
기능: 폴더를 선택해, 해당 폴더의 데이터를 규칙과 대조하고
      자동으로 관리하는 코드
      각 조건은 개별적으로 적용됩니다.
변수:
    src: 규칙에 따라 자동으로 관리할 파일이 있는 '폴더'
    dest: 규칙에 따라 파일을 이동할 '폴더'
    condition : 사용 가능한 조건
    behaviors : 사용 가능한 행동

    rulepath : 규칙 파일을 생성하고 읽어들이는 경로
"""

condition = ['크기', '확장자', '접근시간']
behaviors = ['이동', '삭제']
rulepath = os.path.join('.\Control', 'Rule.txt')


def AutoFileManager():
    """
    파일 자동 관리자를 실행하는 메인 함수
    """
    end = False
    managerExecute()
    while not end:
        
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")

        if select == '?':
            print("""
도움말
파일 자동 관리를 위해 규칙을 지정하고, 실행할 수 있습니다.
규칙의 각 조건은 개별적으로 적용됩니다.
                  
'추가' : 파일 자동 관리를 위한 규칙을 추가합니다.
'삭제' : 파일 자동 관리를 위한 규칙을 삭제합니다.
'실행' : 규칙에 맞는 파일 관리를 임의 실행합니다.
'종료' : 프로그램을 종료합니다.""")

        elif select == '추가':
            src = input("규칙을 적용할 폴더의 경로를 입력하세요 : ")
            rList = input(f"""
규칙을 공백으로 구분해서 입력해주세요.(ex : 이동 크기 >20 확장자 .txt)
가능한 행동 : 이동, 삭제
가능한 규칙 : 크기(MB), 확장자, 접근시간(접근 이후부터의 시간)
""").split()
            dest = ""
            if rList[0] == "이동":
                dest = input("규칙에 의해 이동할 폴더의 경로를 입력하세요 : ")
            if len(rList)<3:
                print("올바른 규칙이 입력되지 않았습니다.")
                continue
            rule = {rList[i+1]: rList[i+2] for i in range(0, len(rList)-1, 2)}
            print(rule)
            if Rintegrity(src, dest, rList[0], rule):
                addRule(src, dest, rList[0], rule)

        elif select == '삭제':
            printRule()
            removeRule(input("""변경할 파일들의 번호를 변경하고 싶은 순서대로, 공백 문자 혹은 -로 구분해 입력 
                  (ex: 1 3-20 21 22): """))

        elif select == '실행':
            managerExecute()

        elif select == "종료":
            print("자동 파일 관리자를 종료합니다.")
            end = True

        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")


# 규칙이 조건을 만족하는 지 확인하는 함수
def Rintegrity(src, dest, behave, rule):
    
    try:
        if os.path.exists(src) and (os.path.exists(dest) if dest!="" else True):
            if behave in behaviors:
                for key, value in rule.items():
                    if key =='크기':
                        if re.match(r'[<>]=?\d*\.?\d+', value):
                            print("규칙을 성공적으로 추가했습니다.")
                            return True
                    if key =='확장자':
                        if re.match(r'[a-zA-Z]{0,3}$', value):
                            print("규칙을 성공적으로 추가했습니다.")
                            return True
                    if key =='접근시간':
                        if re.match(r'[<>]=?\d+', value):
                            print("규칙을 성공적으로 추가했습니다.")
                            return True
                    
        print("규칙을 추가하던 도중 오류가 발생했습니다.")
        return False
    except:
        print("규칙을 추가하던 도중 오류가 발생했습니다.")
        return False

# 규칙을 추가하는 함수
def addRule(src, dest, behave, rule):
    try:
        if not os.path.exists(rulepath):
            # 규칙 파일이 존재하지 않으면 파일을 생성합니다.
            with open(rulepath, 'w') as file:
                file.write('')
            print('Rule 파일을 생성했습니다.')

    except:
        print("Rule.txt를 생성할 수 없거나 권한이 없습니다.")

    # 규칙 데이터를 한 줄에 저장합니다.
    rulestring = f"{src}/{dest}/{behave}/"
    for key, value in rule.items():
        if key in condition:
            rulestring += f"'{key}':'{value}',"
    try:
        with open(rulepath, 'a') as file:
            file.write(rulestring[:-1]+'\n')
    except:
        print("규칙을 추가할 수 없거나 수정할 권한이 없습니다.")

# 파일에서 규칙 데이터를 읽어들여 출력하는 함수
def printRule():
    try:
        with open(rulepath, 'r') as file:
            for index, line in enumerate(file.readlines(), 1):
                print(f"{index}. {line[:-1]}")
    except:
        print("규칙 파일을 열 수 없거나 권한이 없습니다.")

# 파일에서 규칙 데이터를 읽어들여 특정 줄의 규칙을 삭제하는 코드
def removeRule(num):
    indexList = []
    for x in num.split():
        if re.match(r'^\d+$|^\d+-\d+$', x):  # 숫자 또는 숫자-숫자 형식의 입력 검증
            if '-' in x:
                start, end = x.split('-')
                indexList.extend([x for x in range(int(start)-1, int(end))])
            else:
                indexList.append(int(x)-1)
        else:
            print("입력된 파일 번호가 문자이거나 정상적이지 않습니다.")
            return

    # 파일에서 규칙 데이터를 읽어들여 유효성을 검사하고 삭제
    try:
        with open(rulepath, 'r') as file:
            lines = file.readlines()
        for index in indexList:
            if 0 <= index < len(lines):
                del lines[index]

                # 수정된 내용을 파일에 다시 작성
                with open(rulepath, 'w') as file:
                    file.writelines(lines)
            else:
                print(f"{index+1}번째 라인을 삭제할 수 없습니다.")
    except:
        print("규칙 파일을 편집할 수 없거나 권한이 없습니다.")
    
# 규칙 파일을 읽어와 해당 규칙대로 파일을 관리하는 실행 함수
def managerExecute():
    try:
        # 규칙 파일에서 데이터를 읽어오기
        with open(rulepath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                src, dest, behave, rule = line.split('/')
                rule = json.loads("{" + rule.replace('\n', '').replace("'", '"') + "}")

                # 지정된 경로에서 파일 목록을 가져와 조건에 따라 필터링
                files = [os.path.join(src, f) for f in (os.listdir(src))]
                result = set()

                if '크기' in rule:
                    if re.match(r'([<>]=?\d+|==\d+)', rule.get('크기', 0)):
                        # 파일을 불러와 조건에 따라 파일을 필터링
                        for file in files:
                            file_path = os.path.join(src, file)
                            size = os.path.getsize(file_path) / (1024 * 1024)  # 파일 크기를 MB로 변환

                            if eval(f"{size}{rule['크기']}"):
                                result.add(file_path)

                if '확장자' in rule:
                    if re.match(r'[a-zA-Z]{0,3}$', rule.get('확장자', 0)):
                        # 파일을 불러와 조건에 따라 파일을 필터링
                        for file in files:
                            file_path = os.path.join(src, file)
                            _, extension = os.path.splitext(file_path) # 확장자 추출
                            if eval(f"'{extension}'=='.{rule['확장자']}'"):
                                result.add(file_path)

                if '접근시간' in rule:
                    if re.match(r'[<>]=?\d+', rule.get('접근시간', 0)):
                        # 파일을 불러와 조건에 따라 파일을 필터링
                        for file in files:
                            file_path = os.path.join(src, file)
                            abandon = int(re.findall(r'\d+', rule['접근시간'])[0]) * 24 * 60 * 60  # 삭제할 시간 설정
                            if eval(f"{time.time()-os.path.getatime(file_path)}{re.findall(r'[<>]=?', rule.get('접근시간', 0))[0]}{abandon}"):
                                result.add(file_path)

                # 설정된 행동에 따라 이동 혹은 삭제
                if behave=="이동":
                    for file_path in list(result):
                        shutil.move(file_path, dest)
                elif behave=="삭제":
                    for file_path in list(result):
                        os.remove(file_path)
    except:
        print("오류가 발생했습니다.")