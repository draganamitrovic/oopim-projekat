# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Student(object):
    def setupUi(self, Student):
        Student.setObjectName("Student")
        Student.resize(639, 484)
        self.title_2 = QtWidgets.QLabel(Student)
        self.title_2.setGeometry(QtCore.QRect(40, 10, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_2.setObjectName("title_2")
        self.lista_ponuda_label = QtWidgets.QLabel(Student)
        self.lista_ponuda_label.setGeometry(QtCore.QRect(450, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lista_ponuda_label.setFont(font)
        self.lista_ponuda_label.setObjectName("lista_ponuda_label")
        self.about = QtWidgets.QTextBrowser(Student)
        self.about.setGeometry(QtCore.QRect(30, 70, 301, 111))
        self.about.setAutoFillBackground(False)
        self.about.setObjectName("about")
        self.lista_ponuda = QtWidgets.QListView(Student)
        self.lista_ponuda.setGeometry(QtCore.QRect(350, 110, 281, 331))
        self.lista_ponuda.setObjectName("lista_ponuda")
        self.details_btn_ponude = QtWidgets.QPushButton(Student)
        self.details_btn_ponude.setGeometry(QtCore.QRect(540, 450, 75, 23))
        self.details_btn_ponude.setObjectName("details_btn_ponude")
        self.logout_btn = QtWidgets.QPushButton(Student)
        self.logout_btn.setGeometry(QtCore.QRect(540, 10, 75, 23))
        self.logout_btn.setObjectName("logout_btn")
        self.calendarWidget = QtWidgets.QCalendarWidget(Student)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 230, 321, 191))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Student)
        QtCore.QMetaObject.connectSlotsByName(Student)

    def retranslateUi(self, Student):
        _translate = QtCore.QCoreApplication.translate
        Student.setWindowTitle(_translate("Student", "Dialog"))
        self.title_2.setText(_translate("Student", "StudentTourist"))
        self.lista_ponuda_label.setText(_translate("Student", "Lista ponuda"))
        self.about.setHtml(_translate("Student", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">StudentTourist je studentska organizacija koja nudi izlete i ekskurzije za sve studente. Ovde mo┼¥ete pregledati listu svih ponuda na┼íe turisti─ìke organizacije. Za vi┼íe detalja i prijavljivanje, selektujte ponudu sa liste i kliknite dugme Detaljnije.</span></p></body></html>"))
        self.details_btn_ponude.setText(_translate("Student", "Detaljnije"))
        self.logout_btn.setText(_translate("Student", "Odjavi se"))

