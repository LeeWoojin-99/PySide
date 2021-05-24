import sys
from PySide6.QtWidgets import *

#app = QApplication(sys.argv)
app = QApplication()
# 우리가 제작한 GUI를 움직이게 해주는 클래스 QApplication
# 프로그램 내에서 꼭 한 번 실행되어야 하며, 한 개의 인스턴스만 존재할 수 있다.
# 밑에 나오는 app.exec() 메소드를 실행해서 이벤트 루프를 시작시킨다.
# 이벤트 루프가 진행되고 있는 동안 상호 작용이 가능하다.
# 여기서 상호 작용이란 GUI 윈도우가 반응할 수 있는 모든 작업을 일컫는다.

window = QWidget()
#window = QMainWindow()
# 빈 창 위젯을 생성하는 QWidget()

window.show()
# .show() : 만든 위젯 창을 나타나게 하는 역할

app.exec()
# app.exec()를 실행해야 이벤트 루프가 시작된다.
# 이벤트 루프가 시작되지 않으면 응답없음 상태로 있는다.
# 이 명령어를 실행하는 시점에서 우리가 만든 GUI 윈도우가 반응하고 움직이기 시작한다.