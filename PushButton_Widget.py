from PySide6.QtWidgets import *
from PySide6.QtCore import QSize

app = QApplication()
# 이벤트 루프를 담당하는 클래스 QApplication

window = QMainWindow()
# 윈도우 위젯을 생성한다.
window.setWindowTitle("title")
# 윈도우 창의 이름을 설정한다.
window.setFixedSize(QSize(500, 300))
# 위젯의 창 크기를 width 500, height 300로 한다.

button = QPushButton(text = 'Push Button')
# PushButton 위젯을 생성한다. 안의 글자는 'Push Button'을 넣는다.

button = QPushButton(text = 'Push Button', parent = window)
# window 위젯을 부모로 하는 PushButton 위젯이다.

#window.setCentralWidget(button)
# 위젯 센터에 위치할 위젯을 직접 고른다.
# window 위젯의 중앙에 button 위젯을 위치하도록 한다.

window.show()
# 해당 위젯을 보여준다.

app.exec()
# 이벤트 루프를 시작한다.