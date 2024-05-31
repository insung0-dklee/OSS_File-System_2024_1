'''
즐겨찾기 기능 패키지
'''

from typing import List


def bookmark(bookmark : List):

    finish = False
    while not finish:

        select = input("원하는 기능을 입력하세요. ('?' 입력시 도움말)")
        
        if select == '?':
            print(" '목록' 을 입력하면 현재 즐겨찾기 목록을 볼 수 있습니다.")
            print(" '추가' 를 입력하면 즐겨찾기를 목록에 추가할 수 있습니다.")

        elif select == '목록':
            showFavorites(bookmark)

        elif select == '추가':
            addFavorite(bookmark)

        elif select == "나가기":
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