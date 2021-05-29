'''
메모장 열기와 저장 구현
'''

from PySide6.QtWidgets import *
from ui_메모장 import Ui_MainWindow

class MainWindow1(QMainWindow, Ui_MainWindow):
    # Ui_MainWindow를 상속함으로써 만든 ui를 사용한다.

    def __init__(self):
        super(MainWindow1, self).__init__()
        # 상위 클래스의 생성자 실행
        self.setupUi(self)

        self.action_O.triggered.connect(self.open_file)
        # action_W 위젯의 트리거가 발생되면 해당 함수를 실행한다.
        self.action_S.triggered.connect(self.save_file)
        # action_W 위젯의 트리거가 발생되면 해당 함수를 실행한다.


    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self)
        # 열고자 하는 텍스트 파일을 선택
        # 0번 인덱스의 값은 파일의 이름
        if file_name[0]:
            with open(file_name[0], encoding='UTF-8') as f:
                text = f.read()
                # 파일의 값을 text 변수에 대입
            self.plainTextEdit.setPlainText(text)
            # 가져온 값을 

    def save_file(self):
        file_name = QFileDialog.getOpenFileName(self)
        # 저장하고자 하는 텍스트 파일을 선택
        if file_name[0]:
            text = self.plainTextEdit.toPlainText()
            # plainTextEdit 위젯에 적혀있는 글자들을 가져와서 text 변수에 대입한다.
            with open(file_name[0], 'w', encoding='UTF-8') as f:
                f.write(text) # 선택했던 텍스트 파일에 text 변수의 값을 쓰고 저장한다.
                # a : 추가 모드 : 파일의 마지막에 새로운 내용을 추가시킬 때 사용
                # w : 쓰기 모드 : 파일에 내용을 새롭게 쓸 때 사용

app = QApplication()
window = MainWindow1()
window.show()
app.exec()