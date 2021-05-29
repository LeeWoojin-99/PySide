from PySide6.QtWidgets import *

app = QApplication()
window = QMainWindow()

window.setCentralWidget(QPlainTextEdit())

window.show()
app.exec()