# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
coding
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(519, 487)
        self.title_2 = QtWidgets.QLabel(Admin)
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
        self.tabs_admin = QtWidgets.QTabWidget(Admin)
        self.tabs_admin.setGeometry(QtCore.QRect(40, 100, 441, 371))
        self.tabs_admin.setObjectName("tabs_admin")
        self.student_tab_admin = QtWidgets.QWidget()
        self.student_tab_admin.setObjectName("student_tab_admin")
        self.delete_student_btn_admin = QtWidgets.QPushButton(self.student_tab_admin)
        self.delete_student_btn_admin.setGeometry(QtCore.QRect(340, 300, 75, 23))
        self.delete_student_btn_admin.setObjectName("delete_student_btn_admin")
        self.listastudenata_list_admin = QtWidgets.QListWidget(self.student_tab_admin)
        self.listastudenata_list_admin.setGeometry(QtCore.QRect(30, 50, 361, 231))
        self.listastudenata_list_admin.setObjectName("listastudenata_list_admin")
        self.add_student_btn_admin = QtWidgets.QPushButton(self.student_tab_admin)
        self.add_student_btn_admin.setGeometry(QtCore.QRect(250, 300, 75, 23))
        self.add_student_btn_admin.setObjectName("add_student_btn_admin")
        self.listastudenata_label = QtWidgets.QLabel(self.student_tab_admin)
        self.listastudenata_label.setGeometry(QtCore.QRect(160, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listastudenata_label.setFont(font)
        self.listastudenata_label.setObjectName("listastudenata_label")
        self.tabs_admin.addTab(self.student_tab_admin, "")
        self.organizator_tab_admin = QtWidgets.QWidget()
        self.organizator_tab_admin.setObjectName("organizator_tab_admin")
        self.listaorganizarora_label = QtWidgets.QLabel(self.organizator_tab_admin)
        self.listaorganizarora_label.setGeometry(QtCore.QRect(160, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listaorganizatora_label.setFont(font)
        self.listaorganizatora_label.setObjectName("listaorganizatora_label")
        self.listWidget_2 = QtWidgets.QListWidget(self.organizator_tab_admin)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 50, 361, 231))
        self.listWidget_2.setObjectName("listWidget_2")
        self.add_organizator_btn_admin = QtWidgets.QPushButton(self.organizator_tab_admin)
        self.add_organizator_btn_admin.setGeometry(QtCore.QRect(250, 300, 75, 23))
        self.add_organizator_btn_admin.setObjectName("add_organizator_btn_admin")
        self.delete_organizator_btn_admin = QtWidgets.QPushButton(self.organizator_tab_admin)
        self.delete_organizator_btn_admin.setGeometry(QtCore.QRect(340, 300, 75, 23))
        self.delete_organizator_btn_admin.setObjectName("delete_organizator_btn_admin")
        self.tabs_admin.addTab(self.organizator_tab_admin, "")
        self.ponuda_tab_admin = QtWidgets.QWidget()
        self.ponuda_tab_admin.setObjectName("ponuda_tab_admin")
        self.listaponuda_label = QtWidgets.QLabel(self.ponuda_tab_admin)
        self.listaponuda_label.setGeometry(QtCore.QRect(160, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listaponuda_label.setFont(font)
        self.listaponuda_label.setObjectName("listaponuda_label")
        self.listaponuda_list_admin = QtWidgets.QListWidget(self.ponuda_tab_admin)
        self.listaponuda_list_admin.setGeometry(QtCore.QRect(30, 50, 361, 231))
        self.listaponuda_list_admin.setObjectName("listaponuda_list_admin")
        self.add_ponuda_btn_admin = QtWidgets.QPushButton(self.ponuda_tab_admin)
        self.add_ponuda_btn_admin.setGeometry(QtCore.QRect(250, 300, 75, 23))
        self.add_ponuda_btn_admin.setObjectName("add_ponuda_btn_admin")
        self.delete_ponuda_btn_admin = QtWidgets.QPushButton(self.ponuda_tab_admin)
        self.delete_ponuda_btn_admin.setGeometry(QtCore.QRect(340, 300, 75, 23))
        self.delete_ponuda_btn_admin.setObjectName("delete_ponuda_btn_admin")
        self.tabs_admin.addTab(self.ponuda_tab_admin, "")
        self.logout_btn = QtWidgets.QPushButton(Admin)
        self.logout_btn.setGeometry(QtCore.QRect(420, 10, 75, 23))
        self.logout_btn.setObjectName("logout_btn")

        self.retranslateUi(Admin)
        self.tabs_admin.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Dialog"))
        self.title_2.setText(_translate("Admin", "StudentTourist"))
        self.delete_student_btn_admin.setText(_translate("Admin", "Obrisi"))
        self.add_student_btn_admin.setText(_translate("Admin", "Dodaj"))
        self.listastudenata_label.setText(_translate("Admin", "Lista studenata"))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.student_tab_admin), _translate("Admin", "Studenti"))
        self.listaorganizarora_label.setText(_translate("Admin", "Lista organizatora"))
        self.add_organizator_btn_admin.setText(_translate("Admin", "Dodaj"))
        self.delete_organizator_btn_admin.setText(_translate("Admin", "Obrisi"))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.organizator_tab_admin), _translate("Admin", "Organizatori"))
        self.listaponuda_label.setText(_translate("Admin", "Lista ponuda"))
        self.add_ponuda_btn_admin.setText(_translate("Admin", "Dodaj"))
        self.delete_ponuda_btn_admin.setText(_translate("Admin", "Obrisi"))
        self.tabs_admin.setTabText(self.tabs_admin.indexOf(self.ponuda_tab_admin), _translate("Admin", "Ponude"))
        self.logout_btn.setText(_translate("Admin", "Odjavi se"))

