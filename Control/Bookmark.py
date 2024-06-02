'''
즐겨찾기 기능 패키지
'''

import os
import shutil
from typing import List
from Control import FileEdit


favorites = []

def bookmark(bookmark : List):

    finish = False
    while not finish:
        collect_favorite_file()
        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")
        
        if select == '?':
            print(" '목록' 입력시 현재 즐겨찾기 목록을 볼 수 있습니다.")
            print(" '추가' 입력시 즐겨찾기를 목록에 추가할 수 있습니다.")
            print(" '삭제' 입력시 즐겨찾기 목록을 지울 수 있습니다.")
            print(" '종료' 입력시 프로그램을 종료할 수 있습니다.")

        elif select == '목록':
            showFavorites(bookmark)

        elif select == '추가':
            addFavorite(bookmark)

        elif select =='삭제':
            removeFavorite(bookmark)

        elif select == "종료":
            print("즐겨찾기를 종료합니다.")
            finish = True
        
        else:
            print("잘못 입력하셨습니다. 다시 입력해주세요.")

def showFavorites(bookmark: List):
    if not bookmark:
        print("현재 즐겨찾기 목록이 비어있습니다.")
    else:
        print("즐겨찾기 목록:")
        for i, favorite in enumerate(bookmark, 1):
            print(f"{i}. {favorite}")

def addFavorite(bookmark: List):
    path = input("즐겨찾기에 추가할 파일 경로를 입력하세요: ")
    bookmark.append(path)
    print("즐겨찾기에 추가되었습니다.")

def removeFavorite(bookmark: List):
    """
    즐겨찾기 목록에 파일이 존재한다면 파일 번호를 포함한 즐겨찾기 목록을 출력
    제거할 파일의 번호를 입력받은 후, 해당 파일을 제거
    """
    favorites = bookmark
    if not favorites:
        print("현재 즐겨찾기 목록이 비어있습니다.")
    else:
        print("즐겨찾기 목록:")
        for i, favorite in enumerate(favorites, 1):
            print(f"{i}. {favorite}")

        index = int(input("제거할 파일의 번호를 입력하세요: "))
        if 1 <= index <= len(favorites):
            removed_favorite = favorites.pop(index - 1)
            print(f"{removed_favorite} 가 즐겨찾기에서 제거되었습니다.")
        else:
            print("해당 번호의 파일이 존재하지 않습니다. 제거할 파일의 번호를 다시 입력해주세요.")

def collect_favorite_file(bookmark: List):
    '''
    북마크에 등록된 파일들만 모아두는 디렉토리 생성
    북마크에 파일이 지워지면 자동으로 그것이 반영됨.
    bookmark : 북마크 리스트에 있는 경로를 참고해서 링크를 가져옴.
    '''
    bookmark_dir = './bookmakr'
    if not os.path.exists(bookmark_dir):
        os.makedirs(bookmark_dir)
    else:
        shutil.rmtree(bookmark_dir)
        os.makedirs(bookmark_dir)

    try:
        for i, mark in enumerate(bookmark,1):
            FileEdit.create_symLink(favorites, i)
    except:
        print("에러가 발생했습니다.")