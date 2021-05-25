'''
Push Btn을 이용한 Signal and Slot 알아보기
'''

from PySide6.QtWidgets import *

def button_is_clicked():
	print("Clicked!")
def button_is_pressed():
	print("Pressed!")
def button_is_released():
	print("Released!")

app = QApplication()
window = QMainWindow()
button = QPushButton("Press Me!")

button.clicked.connect(button_is_clicked) # 버튼을 클릭한다면 해당 함수를 실행
button.pressed.connect(button_is_pressed) # 버튼을 누를 때 해당 함수를 실행
button.released.connect(button_is_released) # 버튼을 눌렀다가 땔 때 해당 함수를 실행
window.setCentralWidget(button)

window.show()
app.exec()

print("program exit")