'''
GUI를 통한 파일 시스템 활용
'''


import os
import tkinter



def gui_main():
    def pwd():
        '''
        현위치를 지속적으로 출력하여 보여준다.
        '''
        return os.getcwd()

    def yshell_help():
        yshell_help_window = tkinter.Toplevel()
        yshell_help_window.title("yshell 도움말")
        text = """
        ==========================================================
        [도움말]
        '파일편집'           입력시 파일을 편집할 수 있습니다.
        '즐겨찾기'           입력시 즐겨찾기 기능을 사용할 수 있습니다.
        '파일관리'           입력시 파일을 관리할 수 있습니다.
        '가독성'             입력시 파일의 단위를 읽기 좋게 볼 수 있습니다.
        '중복관리'           입력시 중복 파일을 관리할 수 있습니다.
        '종료'               입력시 프로그램을 종료합니다.
        '메타데이터 출력'    입력시 해당 파일 메타 데이터 확인
        '파일삭제'           입력시 해당 파일 삭제
        '파일검색'           입력시 원하는 파일의 위치 검색
        '파일이동'           입력시 파일을 원하는 디렉토리로 이동
        '디렉토리 생성'      입력시 원하는 경로에 디렉토리 생성
        '파일목록'           입력시 해당 디렉토리의 파일의 목록 출력
        '부모 디렉토리 확인' 입력시 선택한 디렉토리의 부모 디렉토리 출력
        '파일복사'           입력시 파일 복사 및 붙여넣기
        '잘라내기'           입력시 파일 잘라내기 및 붙여넣기
        '파일생성'           입력시 현재 디렉토리에 빈 파일을 생성한다.
        '종료'               입력시 프로그램을 종료할 수 있습니다.
        ==========================================================
                """
        label = label = tkinter.Label(yshell_help_window, text=text)
        label.pack()
        
    window = tkinter.Tk()

    window.title("yshell")
    window.geometry("800x600+200+200")
    window.resizable(True, True)

    pwd = pwd()
    pwd = tkinter.Label(window, text = f'현재경로 : {pwd}')
    pwd.pack(anchor='nw')

    yshell_help = tkinter.Button(window, text = '도움말', command=yshell_help)
    yshell_help.pack()

    window.mainloop()
