# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PonudaDesc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PonudaDesc(object):
    def setupUi(self, PonudaDesc):
        PonudaDesc.setObjectName("PonudaDesc")
        PonudaDesc.resize(351, 402)
        self.desc_input_ponuda = QtWidgets.QPlainTextEdit(PonudaDesc)
        self.desc_input_ponuda.setGeometry(QtCore.QRect(120, 210, 171, 121))
        self.desc_input_ponuda.setObjectName("desc_input_ponuda")
        self.name_input_ponuda = QtWidgets.QLineEdit(PonudaDesc)
        self.name_input_ponuda.setGeometry(QtCore.QRect(120, 80, 171, 20))
        self.name_input_ponuda.setObjectName("name_input_ponuda")
        self.place_input_ponuda = QtWidgets.QLineEdit(PonudaDesc)
        self.place_input_ponuda.setGeometry(QtCore.QRect(120, 140, 171, 20))
        self.place_input_ponuda.setObjectName("place_input_ponuda")
        self.back_btn_newponuda = QtWidgets.QPushButton(PonudaDesc)
        self.back_btn_newponuda.setGeometry(QtCore.QRect(246, 350, 75, 23))
        self.back_btn_newponuda.setObjectName("back_btn_newponuda")
        self.time_input_ponuda = QtWidgets.QDateTimeEdit(PonudaDesc)
        self.time_input_ponuda.setGeometry(QtCore.QRect(120, 110, 171, 22))
        self.time_input_ponuda.setObjectName("time_input_ponuda")
        self.name_label = QtWidgets.QLabel(PonudaDesc)
        self.name_label.setGeometry(QtCore.QRect(60, 80, 41, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.time_label = QtWidgets.QLabel(PonudaDesc)
        self.time_label.setGeometry(QtCore.QRect(60, 110, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.place_label = QtWidgets.QLabel(PonudaDesc)
        self.place_label.setGeometry(QtCore.QRect(60, 140, 41, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.place_label.setFont(font)
        self.place_label.setObjectName("place_label")
        self.price_label = QtWidgets.QLabel(PonudaDesc)
        self.price_label.setGeometry(QtCore.QRect(60, 170, 41, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.price_label.setFont(font)
        self.price_label.setObjectName("price_label")
        self.prijavise_btn_ponuda = QtWidgets.QPushButton(PonudaDesc)
        self.prijavise_btn_ponuda.setGeometry(QtCore.QRect(150, 350, 81, 23))
        self.prijavise_btn_ponuda.setObjectName("prijavise_btn_ponuda")
        self.desc_label = QtWidgets.QLabel(PonudaDesc)
        self.desc_label.setGeometry(QtCore.QRect(60, 210, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.desc_label.setFont(font)
        self.desc_label.setObjectName("desc_label")
        self.price_input_ponuda = QtWidgets.QLineEdit(PonudaDesc)
        self.price_input_ponuda.setGeometry(QtCore.QRect(120, 170, 171, 20))
        self.price_input_ponuda.setObjectName("price_input_ponuda")
        self.title = QtWidgets.QLabel(PonudaDesc)
        self.title.setGeometry(QtCore.QRect(20, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setObjectName("title")

        self.retranslateUi(PonudaDesc)
        QtCore.QMetaObject.connectSlotsByName(PonudaDesc)

    def retranslateUi(self, PonudaDesc):
        _translate = QtCore.QCoreApplication.translate
        PonudaDesc.setWindowTitle(_translate("PonudaDesc", "Dialog"))
        self.back_btn_newponuda.setText(_translate("PonudaDesc", "Nazad"))
        self.name_label.setText(_translate("PonudaDesc", "Naziv"))
        self.time_label.setText(_translate("PonudaDesc", "Vreme"))
        self.place_label.setText(_translate("PonudaDesc", "Mesto"))
        self.price_label.setText(_translate("PonudaDesc", "Cena"))
        self.prijavise_btn_ponuda.setText(_translate("PonudaDesc", "Prijavi se"))
        self.desc_label.setText(_translate("PonudaDesc", "Opis"))
        self.title.setText(_translate("PonudaDesc", "StudentTourist"))

