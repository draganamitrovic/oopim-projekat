# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 300)
        self.username_label = QtWidgets.QLabel(Login)
        self.username_label.setGeometry(QtCore.QRect(60, 170, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Login)
        self.password_label.setGeometry(QtCore.QRect(130, 200, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.password_input = QtWidgets.QLineEdit(Login)
        self.password_input.setGeometry(QtCore.QRect(180, 170, 141, 20))
        self.password_input.setObjectName("password_input")
        self.lineEdit = QtWidgets.QLineEdit(Login)
        self.lineEdit.setGeometry(QtCore.QRect(180, 200, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.login_btn = QtWidgets.QPushButton(Login)
        self.login_btn.setGeometry(QtCore.QRect(290, 250, 75, 23))
        self.login_btn.setObjectName("login_btn")
        self.title_2 = QtWidgets.QLabel(Login)
        self.title_2.setGeometry(QtCore.QRect(40, 70, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_2.setObjectName("title_2")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.username_label.setText(_translate("Login", "Korisni─ìko ime"))
        self.password_label.setText(_translate("Login", "┼áifra"))
        self.login_btn.setText(_translate("Login", "Uloguj se"))
        self.title_2.setText(_translate("Login", "StudentTourist"))

