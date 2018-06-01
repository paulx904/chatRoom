# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc01\Desktop\left.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label.setObjectName("label")
        self.nickname = QtWidgets.QLineEdit(self.centralwidget) #where to input nickname
        self.nickname.setGeometry(QtCore.QRect(60, 10, 121, 21))
        self.nickname.setObjectName("nickname")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 51, 16))
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(self.centralwidget) #where to input password
        self.password.setGeometry(QtCore.QRect(240, 10, 131, 21))
        self.password.setObjectName("password")
        self.add_button = QtWidgets.QPushButton(self.centralwidget) #button to add client
        self.add_button.setGeometry(QtCore.QRect(10, 40, 361, 31))
        self.add_button.setObjectName("add_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget) #button to delete client
        self.delete_button.setGeometry(QtCore.QRect(10, 530, 361, 31))
        self.delete_button.setObjectName("delete_button")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 361, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget) #checkBox : client list
        self.checkBox.setGeometry(QtCore.QRect(20, 90, 73, 16))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "NickName"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.add_button.setText(_translate("MainWindow", "Add"))
        self.delete_button.setText(_translate("MainWindow", "Del"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))

