from PySide6.QtWidgets import *
import sys

print(sys.path)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 상속해준 클래스(QMainWindow)의 생성자(__init__())를 실행하는 부분
        #super().__init__()

        self.button = QPushButton(parent=self)
        # 기존의 코드 : button = QPushButton(parent = window)
        self.setCentralWidget(self.button)
        #window.setCentralWidget(button)
        # self : 클래스의 인스턴스
        # self.button : 인스턴스의 button
        # setCentralWidget 메서드가 실행되며 QPushButton 클래스의 parent 파라미터는 의미가 없어진다.
        # self 위젯의 센터에 위치할 위젯을 self.button으로 한다는 의미이다.
        self.button.setCheckable(True)
        # 일반적인 버튼을 토글 방식의 버튼으로 변경하는 코드
        # 한 번 클릭하면 체크된 채로 유지되고, 다시 한 번 클릭하면 체크 해제되는 방식이다.
        self.button.clicked.connect(self.button_clicked)
        # 버튼이 클릭된다면 해당 슬롯을 실행
        self.click_count = 0
        # 초기 click_count 변수의 값을 0으로 초기화
 
    def button_clicked(self):
        # 버튼이 클릭될 때마다 실행되는 슬롯 메서드
        self.click_count += 1
        self.button.setText("%d번 클릭함"%self.click_count)

app = QApplication()

window = MainWindow()

window.show()

app.exec()