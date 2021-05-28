from PySide6.QtWidgets import *
 
app = QApplication()
window = QMainWindow()

layout = QVBoxLayout()
# V : Vertical : 세로
# 위젯으로 구성하는 레이아웃 박스
# 세로방향으로 위젯을 위에서부터 차례대로 붙일 수 있다.
input_widget = QLineEdit()
label_widget = QLabel()
# textChanged.connect 메서드와 setText 메서드에서 사용되기 위해서 변수로 만들어 사용
layout.addWidget(input_widget) # input
# addWidget 메서드를 사용하여 다른 위젯을 붙일 수 있다.
# 위젯뿐만 아니라 다른 레이아웃 위젯을 붙일 수도 있다.
input_widget.textChanged.connect(label_widget.setText)
layout.addWidget(label_widget) # label

container = QWidget()
# QVBoxLayout과 같은 레이아웃 위젯 단독으로는 메인 윈도우 안에 들어갈 수 없다.
# 컨테이너가 추가로 필요하다. 컨테이너로는 거의 대부분의 경우 QWidget을 사용한다.

# QMainWindow안에는 QWidget을 상속받아 만든 위젯만 들어갈 수 있다.
# QVBoxLayout은 QWidget이 아니라 QLayout을 상속한 클래스이기 때문에
# container라는 QWidget 클래스의 인스턴스를 만들어서 거기에 레이아웃 위젯을 담아 메인 윈도우에 넣는 것이다.
container.setLayout(layout)
# QWidget 인스턴스인 container 안에 layout을 적용한다.
window.setCentralWidget(container)
# container를 QMainWindow 인스턴스인 window의 중앙에 위치시킨다.

window.show()
app.exec()