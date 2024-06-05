import os
import re

#파일 검색 함수 
def search_files(directory, name_pattern, use_regex=False):
    found_files = [] #빈 리스트를 초기화, 찾은 파일들의 경로 저장 

    #os.walkr함수를 사용하여 지정된 디렉토리(폴더)와 하위 디렉토리를 탐색 
    #root : 현재 탐색중인 디렉토리의 경로, 
    #dirs:현재 디렉토리 내의 서브 티렉토리 
    #files : 현재 디렉토리 내의 파일 리스트

    for root, dirs, files in os.walk(directory):
        for file in files:
            if use_regex: 
                #true 
                #파일의 이름이 일치하는 경우, 리스트에 추가
                if re.match(name_pattern, file):
                    found_files.append(os.path.join(root, file))
            else:  #false 
                if file == name_pattern:
                    found_files.append(os.path.join(root, file))
    return found_files

"""
원하는 파일을 찾는 함수.
디렉토리를 순회하면서 파일을 찾아준다.

"""