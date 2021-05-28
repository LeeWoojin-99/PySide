# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'English_Word_Test_Program_UIanzdpN.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(728, 848)
        font = QFont()
        font.setFamilies([u"\ub098\ub214\uc2a4\ud018\uc5b4"])
        font.setPointSize(20)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(57, 57, 57);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 240, 131, 61))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"")
        self.answer_button = QPushButton(self.centralwidget)
        self.answer_button.setObjectName(u"answer_button")
        self.answer_button.setGeometry(QRect(150, 690, 150, 50))
        self.answer_button.setFont(font)
        self.answer_button.setStyleSheet(u"QPushButton{\n"
"background-color: red;\n"
"color: white;\n"
"border: 0px solid black;\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 83, 83);\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(540, 750, 151, 51))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.answer_input = QLineEdit(self.centralwidget)
        self.answer_input.setObjectName(u"answer_input")
        self.answer_input.setGeometry(QRect(200, 310, 300, 77))
        self.answer_input.setFont(font)
        self.answer_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 0px solid black;\n"
"border-radius: 20px;\n"
"padding: 20px 30px;")
        self.result = QTextBrowser(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(190, 510, 361, 161))
        self.result.setFont(font)
        self.result.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 0px solid black;\n"
"border-radius: 20px;\n"
"padding: 20px 30px;")
        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(200, 440, 256, 55))
        self.result_label.setFont(font)
        self.next_problem = QPushButton(self.centralwidget)
        self.next_problem.setObjectName(u"next_problem")
        self.next_problem.setGeometry(QRect(390, 690, 150, 50))
        self.next_problem.setFont(font)
        self.next_problem.setStyleSheet(u"QPushButton{\n"
"background-color: red;\n"
"color: white;\n"
"border: 0px solid black;\n"
"border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 83, 83);\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 40, 191, 61))
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"")
        self.problem = QTextBrowser(self.centralwidget)
        self.problem.setObjectName(u"problem")
        self.problem.setGeometry(QRect(140, 120, 300, 100))
        self.problem.setFont(font)
        self.problem.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 0px solid black;\n"
"border-radius: 20px;\n"
"padding: 20px 30px;\n"
"width: 150px;\n"
"height: 50px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">\uc2dc\ud5d8\uc9c0</span></p></body></html>", None))
        self.answer_button.setText(QCoreApplication.translate("MainWindow", u"\ucc44\uc810", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#4b4b4b;\">By \uc774\uc6b0\uc9c4</span></p></body></html>", None))
        self.answer_input.setText("")
        self.result.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub098\ub214\uc2a4\ud018\uc5b4'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">asdsad</span></p></body></html>", None))
        self.result_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">\ucc44\uc810 \uacb0\uacfc</span></p></body></html>", None))
        self.next_problem.setText(QCoreApplication.translate("MainWindow", u"\ub2e4\uc74c \ubb38\uc81c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">\ubb38\uc81c</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.problem.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.problem.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub098\ub214\uc2a4\ud018\uc5b4'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hjkjh</p></body></html>", None))
    # retranslateUi

