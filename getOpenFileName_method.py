from PySide6.QtWidgets import QApplication, QFileDialog
 
app = QApplication()
filename = QFileDialog().getOpenFileName()
# QFileDialog() : getOpenFileName()을 사용할 수 있는 위젯
# getOpenFileName() : 파일 선택시 원소가 두 개인 튜플을 반환하고 선택한 파일명은 0번 인덱스에 있다.
print(filename[0])
app.exec()