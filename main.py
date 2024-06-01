import os

def getParentDir(path):
    return os.path.dirname(path)

import winreg as reg

def toggle_desktop_icons(hide=True):
    # 레지스트리 키 열기
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", 0, reg.KEY_SET_VALUE)
    
    # 바탕화면 아이콘 숨기기 또는 보이기 설정
    # HideIcons 값이 1이면 숨김, 0이면 표시
    reg.SetValueEx(key, "HideIcons", 0, reg.REG_DWORD, 1 if hide else 0)
    
    # 레지스트리 키 닫기
    reg.CloseKey(key)

    # 변경 사항 적용을 위해 Explorer 프로세스 재시작
    import os
    os.system("taskkill /f /im explorer.exe & start explorer")

# 바탕화면 아이콘 숨기기
toggle_desktop_icons(hide=True)

# 바탕화면 아이콘 표시하기
# toggle_desktop_icons(hide=False)

