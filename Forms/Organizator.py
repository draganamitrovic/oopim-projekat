# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Organizator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Organizator(object):
    def setupUi(self, Organizator):
        Organizator.setObjectName("Organizator")
        Organizator.resize(521, 486)
        self.logout_btn = QtWidgets.QPushButton(Organizator)
        self.logout_btn.setGeometry(QtCore.QRect(420, 10, 75, 23))
        self.logout_btn.setObjectName("logout_btn")
        self.title_2 = QtWidgets.QLabel(Organizator)
        self.title_2.setGeometry(QtCore.QRect(110, 50, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title_2.setObjectName("title_2")
        self.tabs_admin = QtWidgets.QTabWidget(Organizator)
        self.tabs_admin.setGeometry(QtCore.QRect(40, 100, 441, 371))
        self.tabs_admin.setObjectName("tabs_admin")
        self.student_tab_organizator = QtWidgets.QWidget()
        self.student_tab_organizator.setObjectName("student_tab_organizator")
        self.delete_student_btn_organizaror = QtWidgets.QPushButton(self.student_tab_organizator)
        self.delete_student_btn_organizaror.setGeometry(QtCore.QRect(340, 300, 75, 23))
        self.delete_student_btn_organizaror.setObjectName("delete_student_btn_organizaror")
        self.listastudenata_list_organizaror = QtWidgets.QListWidget(self.student_tab_organizator)
        self.listastudenata_list_organizaror.setGeometry(QtCore.QRect(30, 50, 361, 231))
        self.listastudenata_list_organizaror.setObjectName("listastudenata_list_organizaror")
        self.add_student_btn_organizaror = QtWidgets.QPushButton(self.student_tab_organizator)
        self.add_student_btn_organizaror.setGeometry(QtCore.QRect(250, 300, 75, 23))
        self.add_student_btn_organizaror.setObjectName("add_student_btn_organizaror")
        self.listastudenata_label = QtWidgets.QLabel(self.student_tab_organizator)
        self.listastudenata_label.setGeometry(QtCore.QRect(160, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listastudenata_label.setFont(font)
        self.listastudenata_label.setObjectName("listastudenata_label")
        self.tabs_admin.addTab(self.student_tab_organizator, "")
        self.ponuda_tab_organizaror = QtWidgets.QWidget()
        self.ponuda_tab_organizaror.setObjectName("ponuda_tab_organizaror")
        self.listaponuda_label = QtWidgets.QLabel(self.ponuda_tab_organizaror)
        self.listaponuda_label.setGeometry(QtCore.QRect(160, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listaponuda_label.setFont(font)
        self.listaponuda_label.setObjectName("listaponuda_label")
        self.listaponuda_list_organizaror = QtWidgets.QListWidget(self.ponuda_tab_organizaror)
        self.listaponuda_list_organizaror.setGeometry(QtCore.QRect(30, 50, 361, 231))
        self.listaponuda_list_organizaror.setObjectName("listaponuda_list_organizaror")
        self.add_ponuda_btn_organizaror = QtWidgets.QPushButton(self.ponuda_tab_organizaror)
        self.add_ponuda_btn_organizaror.setGeometry(QtCore.QRect(250, 300, 75, 23))
        self.add_ponuda_btn_organizaror.setObjectName("add_ponuda_btn_organizaror")
        self.delete_ponuda_btn_organizaror = QtWidgets.QPushButton(self.ponuda_tab_organizaror)
        self.delete_ponuda_btn_organizaror.setGeometry(QtCore.QRect(340, 300, 75, 23))
        self.delete_ponuda_btn_organizaror.setObjectName("delete_ponuda_btn_organizaror")
        self.tabs_admin.addTab(self.ponuda_tab_organizaror, "")

        self.retranslateUi(Organizator)
        self.tabs_admin.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Organizator)

    def retranslateUi(self, Organizator):
        _translate = QtCore.QCoreApplication.translate
        Organizator.setWindowTitle(_translate("Organizator", "Dialog"))
        self.logout_btn.setText(_translate("Organizator", "Odjavi se"))
        self.title_2.setText(_translate("Organizator", "StudentTourist"))
        self.delete_student_btn_organizaror.setText(_translate("Organizator", "Obri┼íi"))
        self.add_student_btn_organizaror.setText(_translate("Organizator", "Dodaj"))
        self.listastudenata_label.setText(_translate("Organizator", "Lista studenata"))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.student_tab_organizator), _translate("Organizator", "Studenti"))
        self.listaponuda_label.setText(_translate("Organizator", "Lista ponuda"))
        self.add_ponuda_btn_organizaror.setText(_translate("Organizator", "Dodaj"))
        self.delete_ponuda_btn_organizaror.setText(_translate("Organizator", "Obri┼íi"))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.ponuda_tab_organizaror), _translate("Organizator", "Ponude"))

