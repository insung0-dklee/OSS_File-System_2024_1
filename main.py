import os
import winreg as reg

def getParentDir(path):
    return os.path.dirname(path)

def toggle_desktop_icons(hide=True):
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, reg.KEY_SET_VALUE)
    reg.SetValueEx(key, "HideIcons", 0, reg.REG_DWORD, 1 if hide else 0)
    reg.CloseKey(key)
    os.system("taskkill /f /im explorer.exe & start explorer")

# 파일 이름 변경 함수
def renameFile():
    try:
        srcPath = input("이름을 변경할 파일의 경로 입력: ")
        newName = input("새로운 파일이름 입력: ")
        parentDir = getParentDir(srcPath)
        newPath = os.path.join(parentDir, newName)
        os.rename(srcPath, newPath)
        print("기존경로: ", srcPath, " 바뀐경로: ", newPath, " 변경완료!")
    except Exception as e:
        print("파일이름 변경 중 에러발생", e)

if __name__ == "__main__":
    while True:
        print("--------------------------------")
        print("기능 선택")
        print("--------------------------------")
        print("1. 파일이름 변경")
        print("2. 바탕화면 아이콘 숨기기/표시하기")
        print("0. 종료")
        
        select = input("입력 (0번 입력시, 종료): ")
        print("\n")

        if select == '1':
            renameFile()
        elif select == '2':
            hide = input("아이콘을 숨기시겠습니까? (y/n): ")
            if hide.lower() == 'y':
                toggle_desktop_icons(hide=True)
                print("바탕화면 아이콘을 숨겼습니다.")
            else:
                toggle_desktop_icons(hide=False)
                print("바탕화면 아이콘을 표시했습니다.")
        elif select == '0':
            print("종료")
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")