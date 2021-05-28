'''
메모장 새창 열기 구현
'''

from PySide6.QtWidgets import *
from ui_메모장 import Ui_MainWindow

class MainWindow1(QMainWindow, Ui_MainWindow):
    # Ui_MainWindow를 상속함으로써 만든 ui를 사용한다.

    def __init__(self):
        super(MainWindow1, self).__init__()
        # 상위 클래스의 생성자 실행
        self.setupUi(self)

        self.new_window.triggered.connect(self.add_window)
        # new_window 객체의 트리거가 발생되면 해당 함수를 실행한다.
        self.windows = []

    def add_window(self):
        add_window = MainWindow1()
        self.windows.append(add_window)
        add_window.show()

app = QApplication()
window = MainWindow1()
window.show()
app.exec()