# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(421, 363)
        self.title = QtWidgets.QLabel(Register)
        self.title.setGeometry(QtCore.QRect(50, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setObjectName("title")
        self.adress_input_reg = QtWidgets.QLineEdit(Register)
        self.adress_input_reg.setGeometry(QtCore.QRect(200, 270, 141, 20))
        self.adress_input_reg.setObjectName("adress_input_reg")
        self.email_label = QtWidgets.QLabel(Register)
        self.email_label.setGeometry(QtCore.QRect(80, 240, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.adress_label = QtWidgets.QLabel(Register)
        self.adress_label.setGeometry(QtCore.QRect(80, 270, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adress_label.setFont(font)
        self.adress_label.setObjectName("adress_label")
        self.email_input_reg = QtWidgets.QLineEdit(Register)
        self.email_input_reg.setGeometry(QtCore.QRect(200, 240, 141, 20))
        self.email_input_reg.setObjectName("email_input_reg")
        self.lastname_input_reg = QtWidgets.QLineEdit(Register)
        self.lastname_input_reg.setGeometry(QtCore.QRect(200, 210, 141, 20))
        self.lastname_input_reg.setObjectName("lastname_input_reg")
        self.name_input_reg_2 = QtWidgets.QLabel(Register)
        self.name_input_reg_2.setGeometry(QtCore.QRect(80, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.name_input_reg_2.setFont(font)
        self.name_input_reg_2.setObjectName("name_input_reg_2")
        self.lastname_label = QtWidgets.QLabel(Register)
        self.lastname_label.setGeometry(QtCore.QRect(80, 210, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lastname_label.setFont(font)
        self.lastname_label.setObjectName("lastname_label")
        self.name_input_reg = QtWidgets.QLineEdit(Register)
        self.name_input_reg.setGeometry(QtCore.QRect(200, 180, 141, 20))
        self.name_input_reg.setObjectName("name_input_reg")
        self.password_label = QtWidgets.QLabel(Register)
        self.password_label.setGeometry(QtCore.QRect(80, 150, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.password_input_reg = QtWidgets.QLineEdit(Register)
        self.password_input_reg.setGeometry(QtCore.QRect(200, 150, 141, 20))
        self.password_input_reg.setObjectName("password_input_reg")
        self.username_label = QtWidgets.QLabel(Register)
        self.username_label.setGeometry(QtCore.QRect(80, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.username_input_reg = QtWidgets.QLineEdit(Register)
        self.username_input_reg.setGeometry(QtCore.QRect(200, 120, 141, 20))
        self.username_input_reg.setObjectName("username_input_reg")
        self.signup_btn_reg = QtWidgets.QPushButton(Register)
        self.signup_btn_reg.setGeometry(QtCore.QRect(204, 320, 101, 23))
        self.signup_btn_reg.setObjectName("signup_btn_reg")
        self.back_to_login_btn = QtWidgets.QPushButton(Register)
        self.back_to_login_btn.setGeometry(QtCore.QRect(320, 320, 75, 23))
        self.back_to_login_btn.setObjectName("back_to_login_btn")
        self.user_type_organizator_reg = QtWidgets.QRadioButton(Register)
        self.user_type_organizator_reg.setGeometry(QtCore.QRect(200, 90, 82, 17))
        self.user_type_organizator_reg.setObjectName("user_type_organizator_reg")
        self.user_type_student_reg = QtWidgets.QRadioButton(Register)
        self.user_type_student_reg.setGeometry(QtCore.QRect(290, 90, 82, 17))
        self.user_type_student_reg.setObjectName("user_type_student_reg")
        self.usertype_label = QtWidgets.QLabel(Register)
        self.usertype_label.setGeometry(QtCore.QRect(80, 90, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.usertype_label.setFont(font)
        self.usertype_label.setObjectName("usertype_label")

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Dialog"))
        self.title.setText(_translate("Register", "StudentTourist"))
        self.email_label.setText(_translate("Register", "Email"))
        self.adress_label.setText(_translate("Register", "Adresa"))
        self.name_input_reg_2.setText(_translate("Register", "Ime"))
        self.lastname_label.setText(_translate("Register", "Prezime"))
        self.password_label.setText(_translate("Register", "┼áifra"))
        self.username_label.setText(_translate("Register", "Korisni─ìko ime"))
        self.signup_btn_reg.setText(_translate("Register", "Registruj korisnika"))
        self.back_to_login_btn.setText(_translate("Register", "Nazad"))
        self.user_type_organizator_reg.setText(_translate("Register", "Organizator"))
        self.user_type_student_reg.setText(_translate("Register", "Student"))
        self.usertype_label.setText(_translate("Register", "Tip korisnika"))

