from PySide6.QtWidgets import *

app = QApplication()
window = QMainWindow()

layout = QVBoxLayout()
# V : Vertical : 세로
# 위젯으로 구성되는 레이아웃 박스
text_edit = QPlainTextEdit()
layout.addWidget(text_edit)

container = QWidget()
# QVBoxLayout과 같은 레이아웃 위젯 단독으로는 메인 윈도우 안에 들어갈 수 없다.
# 컨테이너가 추가로 필요하다. 컨테이너로는 거의 대부분의 경우 QWidget을 사용한다.

container.setLayout(layout)
# QWidget 인스턴스인 container 안에 layout을 적용한다.
window.setCentralWidget(container)
# container를 QMainWindow 인스턴스인 window의 중앙에 위치시킨다.

window.show()
app.exec()
