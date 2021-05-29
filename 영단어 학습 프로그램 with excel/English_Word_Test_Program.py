from PySide6.QtWidgets import *
from PySide6 import QtCore
from ui_English_Word_Test_Program_UI import Ui_MainWindow
import english_excel_file as excel
import time

class WindowClass(QMainWindow, Ui_MainWindow):
	def __init__(self):
		global english_excel_class

		# 초기 설정
		super(WindowClass, self).__init__()
		self.setupUi(self)

		self.rows = english_excel_class.rows
		self.setWindowTitle("영어 공부를 하자")

		self.answer_button.clicked.connect(self.answer_function)
		# QPushButton 클래스 위젯이 클릭되면 해당 함수를 실행
		self.next_problem.clicked.connect(self.next_problem_function)

		self.problem.setPlainText(english_excel_class.cell_data_func(self.rows[0], 1))
		self.problem.setAlignment(QtCore.Qt.AlignCenter)
		# 가로 가운데 정렬
		#self.problem.setVerticalAlignment(QtCore.Qt.AlignCenter)
		# 처음 문제를 QLabel 클래스 위젯에 출력
		self.result.setPlainText("초기 상태")

		self.answer_input.returnPressed.connect(self.answer_function)
		# QLineEdit 클래스 위젯에서 Enter키가 눌릴 때마다 해당 함수를 실행

	def answer_function(self):
		# 시험지에 적혀있는 것이 정답인지 채점하는 함수

		if len(self.rows) == 0:
			# 남아있는 문제가 없다면
			self.answer_input.clear()
			return 0

		if self.answer_input.text() == english_excel_class.cell_data_func(self.rows[0], 2):
			# 정답인 경우

			print("정답")
			#self.result.setPlainText("정답입니다.\n2초 후에 다음문제로 넘어갑니다.")
			#time.sleep(2)
			self.result.setPlainText("정답\n" + english_excel_class.cell_data_func(self.rows[0], 1) + "\n" + english_excel_class.cell_data_func(self.rows[0], 2))
			# 정답이라면 초기 상태로 돌아가기

			# 다음 문제로 넘어가는 과정
			del self.rows[0]
			# 맞춘 문제 지우기

			# 남아있는 문제가 있는지 판별하는 과정
			if len(self.rows) > 0:
				# 마지막 문제
				print("마지막 문제입니다.")
			else:
				# 남아있는 문제가 없는 경우
				self.result.append("문제를 모두 완료하였습니다.")
				#self.result.setAlignment(QtCore.Qt.AlignCenter)
				# 결과 창에 출력
				self.problem.setPlainText("문제를 모두 완료하였습니다.")
				self.problem.setAlignment(QtCore.Qt.AlignCenter)
				# 문제 창에 출력
				self.answer_input.clear()
				return 0

			self.problem.setPlainText(english_excel_class.cell_data_func(self.rows[0], 1))
			self.problem.setAlignment(QtCore.Qt.AlignCenter)
			# 다음 문제 출력

			self.answer_input.clear()
			# 입력 창을 비우기


		else:
			print("오답")
			self.result.setPlainText("오답")
			# 결과 창에 "오답"을 출력
			self.answer_input.clear()
			# 입력 창을 비우기

	def next_problem_function(self):
		if len(self.rows) == 0:
			# 버튼을 눌렀는데 남아있는 문제가 없다면
			self.answer_input.clear()
			return 0

		self.result.setPlainText("다음 문제로 넘어왔습니다.")
		self.result.append("정답\n" + english_excel_class.cell_data_func(self.rows[0], 1) + "\n" + english_excel_class.cell_data_func(self.rows[0], 2))

		del self.rows[0]
		# 넘어간 문제 지우기

		if len(self.rows) == 0:
			# 넘어갔는데 남아있는 문제가 없다면
			self.result.setPlainText("남아있는 문제가 없습니다.")
			self.result.setAlignment(QtCore.Qt.AlignCenter)
			# 결과 창에 출력
			self.problem.setPlainText("남아있는 문제가 없습니다.")
			self.problem.setAlignment(QtCore.Qt.AlignCenter)
			# 문제 창에 출력
			self.answer_input.clear()
			return 0

		self.problem.setPlainText(english_excel_class.cell_data_func(self.rows[0], 1))
		self.problem.setAlignment(QtCore.Qt.AlignCenter)
		# 다음 문제 출력


'''
answer_button : QPushButton
answer_input : QTextEdit
problem_label : QTextBrowser
'''

# 초기 설정값 3개
day = 1
start = 2
end = 5

app = QApplication()
english_excel_class = excel.EnglishExcel(day, start, end)
window = WindowClass()
window.show()
app.exec()

