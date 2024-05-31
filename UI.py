# flake8: noqa
from PyQt5.QtWidgets import QPushButton, QDialog, QDesktopWidget, QVBoxLayout, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QScrollArea, QLineEdit
from PyQt5.QtCore import Qt, QSize
import function
import main

"""
display : 경로를 표시하는 라벨
list_widget : 파일, 폴더 목록을 표시하는 위젯
current : 현재 폴더를 나타내는 탭

refresh(files) : 파일 목록을 입력받아 리스트 위젯을 새로고침하는 함수
"""

#UI를 생성하는 UI 클래스
class UI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        # 시작 시 경로, 파일 목록 초기화
        self.current.display.setText(function.currentDir().replace('\n', ''))
        UI.refresh(self, function.moveDir(function.currentDir()))

    #UI 구성
    def initUI(self):
        self.resize(1000, 750)
        # 각 탭 생성
        self.tabs = QTabWidget()
        self.current = QWidget()
        self.standard(self.current)
        # 레이아웃에 탭 추가 후 출력
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.show()

    #버튼 생성 함수
    def create_button(self, text, size, callback=None):
        button = QPushButton(text)
        button.setFixedSize(size)
        if callback:
            button.clicked.connect(callback)
        return button
        
    #기본 UI
    def standard(self, current):
        
        # 현재 경로를 표시할 디스플레이 생성
        display = QLabel('', current)
        display.setAlignment(Qt.AlignLeft)
        display.setStyleSheet("background-color: #ffffff;"
                              "border: 2px solid black;")
        current.display = display
        
        # 디렉토리의 파일 목록을 출력할 리스트 위젯 생성
        list_widget = QListWidget()
        list_widget.itemDoubleClicked.connect(self.double_clicked)
        current.list_widget = list_widget

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(list_widget)
        
        
        # 기능 실행 버튼 구성
        button_size = QSize(50, 35)

        # 상위 폴더로 돌아가는 버튼
        parent_dir = self.create_button('<-', button_size, lambda: display.setText(UI.refresh(self, function.moveDir(main.getParentDir(function.currentDir())))))

        # GUI 레이아웃 설정
        head = QHBoxLayout()
        head.addWidget(parent_dir)
        head.addWidget(display)

        vbox = QVBoxLayout()
        vbox.addLayout(head)
        vbox.addSpacing(1)
        vbox.addWidget(scroll)

        current.setLayout(vbox)

        self.tabs.addTab(current, '현재 디렉토리')
    
    # 파일 목록을 새로고침하는 함수
    def refresh(self, files):
        self.current.list_widget.clear()
        for file in files:
            item = QListWidgetItem(file)
            self.current.list_widget.addItem(item)

    # 리스트 위젯의 목록이 더블클릭되면 폴더인지 확인하고 경로를 변경하는 함수
    def double_clicked(self, item):
        selected_item = item.text()
        path = function.moveSelected(selected_item)
        if path:
            UI.refresh(self, function.moveDir(path))