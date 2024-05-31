# flake8: noqa
from PyQt5.QtWidgets import QPushButton, QDialog, QDesktopWidget, QVBoxLayout, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QScrollArea, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt, QSize
import function
import main

"""
display : 경로를 표시하는 라벨
list_widget : 파일, 폴더 목록을 표시하는 위젯
current : 현재 폴더를 나타내는 탭
CopyDialog : 복사 기능을 실행하기 위한 새 메세지 창을 생성하는 클래스
CutDialog : 잘라내기 기능을 실행하기 위한 새 메세지 창을 생성하는 클래스
MoveDialog : 이동 기능을 실행하기 위한 새 메세지 창을 생성하는 클래스
DelDialog : 삭제 기능을 실행하기 위한 새 메세지 창을 생성하는 클래스

refresh(files) : 파일 목록을 입력받아 리스트 위젯을 새로고침하는 함수
"""
class CopyDialog(QDialog):
    def __init__(self):
        super(CopyDialog, self).__init__()
        self.initUI()

    def initUI(self):
        # 복사할 파일 경로 입력
        lb1 = QLabel('복사할 파일 경로')
        self.file_path_input = QLineEdit(self)
        line1 = QHBoxLayout()
        line1.addWidget(lb1)
        line1.addWidget(self.file_path_input)

        # 붙여넣을 경로 입력 필드
        lb2 = QLabel('붙여넣을 폴더 경로')
        self.destination_path_input = QLineEdit(self)
        line2 = QHBoxLayout()
        line2.addWidget(lb2)
        line2.addWidget(self.destination_path_input)

        # 확인 버튼
        self.confirm_button = QPushButton('확인', self)
        self.confirm_button.clicked.connect(self.accept)
        layout = QVBoxLayout()
        layout.addLayout(line1)
        layout.addLayout(line2)
        layout.addWidget(self.confirm_button)

        # 레이아웃 설정
        self.setLayout(layout)
        self.setGeometry(500, 500, 500, 300)
        self.setWindowTitle('복사')

    # 입력받은 데이터로 실행
    def execute(self):
        main.copyFile(self.file_path_input.text(), self.destination_path_input.text())
    

class CutDialog(QDialog):
    def __init__(self):
        super(CutDialog, self).__init__()
        self.initUI()

    def initUI(self):
        # 잘라낼 파일 경로 입력
        lb1 = QLabel('잘라낼 파일 경로')
        self.file_path_input = QLineEdit(self)
        line1 = QHBoxLayout()
        line1.addWidget(lb1)
        line1.addWidget(self.file_path_input)

        # 붙여넣을 경로 입력
        lb2 = QLabel('붙여넣을 폴더 경로')
        self.destination_path_input = QLineEdit(self)
        line2 = QHBoxLayout()
        line2.addWidget(lb2)
        line2.addWidget(self.destination_path_input)

        # 확인 버튼
        self.confirm_button = QPushButton('확인', self)
        self.confirm_button.clicked.connect(self.accept)
        layout = QVBoxLayout()
        layout.addLayout(line1)
        layout.addLayout(line2)
        layout.addWidget(self.confirm_button)

        # 레이아웃 설정
        self.setLayout(layout)
        self.setGeometry(500, 500, 500, 300)
        self.setWindowTitle('잘라내기')

    # 입력받은 데이터로 실행
    def execute(self):
        main.cut_file(self.file_path_input.text(), self.destination_path_input.text())

class MoveDialog(QDialog):
    def __init__(self):
        super(MoveDialog, self).__init__()
        self.initUI()

    def initUI(self):
        # 복사할 파일 경로 입력
        lb1 = QLabel('이동할 파일 경로')
        self.file_path_input = QLineEdit(self)
        line1 = QHBoxLayout()
        line1.addWidget(lb1)
        line1.addWidget(self.file_path_input)

        # 붙여넣을 경로 입력 필드
        lb2 = QLabel('붙여넣을 폴더 경로')
        self.destination_path_input = QLineEdit(self)
        line2 = QHBoxLayout()
        line2.addWidget(lb2)
        line2.addWidget(self.destination_path_input)

        # 확인 버튼
        self.confirm_button = QPushButton('확인', self)
        self.confirm_button.clicked.connect(self.accept)
        layout = QVBoxLayout()
        layout.addLayout(line1)
        layout.addLayout(line2)
        layout.addWidget(self.confirm_button)

        # 레이아웃 설정
        self.setLayout(layout)
        self.setGeometry(500, 500, 500, 300)
        self.setWindowTitle('이동')

    # 입력받은 데이터로 실행
    def execute(self):
        main.move_file(self.file_path_input.text(), self.destination_path_input.text())

class DelDialog(QDialog):
    def __init__(self):
        super(DelDialog, self).__init__()
        self.initUI()

    def initUI(self):
        # 복사할 파일 경로 입력
        lb1 = QLabel('삭제할 파일 경로')
        self.file_path_input = QLineEdit(self)
        line1 = QHBoxLayout()
        line1.addWidget(lb1)
        line1.addWidget(self.file_path_input)

        # 확인 버튼
        self.confirm_button = QPushButton('확인', self)
        self.confirm_button.clicked.connect(self.accept)
        layout = QVBoxLayout()
        layout.addLayout(line1)
        layout.addWidget(self.confirm_button)

        # 레이아웃 설정
        self.setLayout(layout)
        self.setGeometry(500, 500, 500, 300)
        self.setWindowTitle('삭제')

    # 입력받은 데이터로 실행
    def execute(self):
        QMessageBox.information(None, "실행 결과", main.delete_file(self.file_path_input.text()))


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

        # 각각 복사, 잘라내기, 이동, 삭제 버튼 생성
        copy = self.create_button('복사', button_size, lambda: self.copy_clicked())
        cut = self.create_button('자르기', button_size, lambda: self.cut_clicked())
        move = self.create_button('이동', button_size, lambda: self.move_clicked())
        delete = self.create_button('삭제', button_size, lambda: self.del_clicked())


        # GUI 레이아웃 설정
        head = QHBoxLayout()
        head.addWidget(parent_dir)
        head.addWidget(display)

        functions = QHBoxLayout()
        functions.addWidget(copy)
        functions.addWidget(cut)
        functions.addWidget(move)
        functions.addWidget(delete)

        vbox = QVBoxLayout()
        vbox.addLayout(head)
        vbox.addSpacing(1)
        vbox.addWidget(scroll)

        vbox.addSpacing(1)
        vbox.addLayout(functions)
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

    # 복사 버튼 클릭 시에 실행될 함수
    def copy_clicked(self):
        dialog = CopyDialog()
        if dialog.exec_() == QDialog.Accepted:
            dialog.execute()
            UI.refresh(self, function.moveDir(function.currentDir()))

    # 잘라내기 버튼 클릭 시에 실행될 함수
    def cut_clicked(self):
        dialog = CutDialog()
        if dialog.exec_() == QDialog.Accepted:
            dialog.execute()
            UI.refresh(self, function.moveDir(function.currentDir()))
    
    # 이동 버튼 클릭 시에 실행될 함수
    def move_clicked(self):
        dialog = MoveDialog()
        if dialog.exec_() == QDialog.Accepted:
            dialog.execute()
            UI.refresh(self, function.moveDir(function.currentDir()))

    # 삭제 버튼 클릭 시에 실행될 함수
    def del_clicked(self):
        dialog = DelDialog()
        if dialog.exec_() == QDialog.Accepted:
            dialog.execute()
            UI.refresh(self, function.moveDir(function.currentDir())) 