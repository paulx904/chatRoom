# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc01\Desktop\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginButton(object):
    def setupUi(self, loginButton):
        loginButton.setObjectName("loginButton")
        loginButton.resize(410, 679)
        self.centralwidget = QtWidgets.QWidget(loginButton)
        self.centralwidget.setObjectName("centralwidget")
        self.chatroom_people = QtWidgets.QTextBrowser(self.centralwidget) #output the number of people in chatroom 
        self.chatroom_people.setGeometry(QtCore.QRect(10, 10, 391, 41))
        self.chatroom_people.setObjectName("chatroom_people")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label.setObjectName("label")
        self.nickName = QtWidgets.QLineEdit(self.centralwidget) #where to input nickname
        self.nickName.setGeometry(QtCore.QRect(70, 60, 121, 41))
        self.nickName.setObjectName("nickName")
        self.password = QtWidgets.QLineEdit(self.centralwidget) #where to input password
        self.password.setGeometry(QtCore.QRect(200, 60, 121, 41))
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget) #button to login
        self.pushButton.setGeometry(QtCore.QRect(330, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 101, 16))
        self.label_2.setObjectName("label_2")
        self.password_change = QtWidgets.QLineEdit(self.centralwidget) #where to input change of password
        self.password_change.setGeometry(QtCore.QRect(110, 110, 211, 41))
        self.password_change.setObjectName("password_change")
        self.password_change_button = QtWidgets.QPushButton(self.centralwidget) #button to change password
        self.password_change_button.setGeometry(QtCore.QRect(330, 120, 75, 23))
        self.password_change_button.setObjectName("password_change_button")
        self.chaty = QtWidgets.QTextBrowser(self.centralwidget) #where to output chatroom message
        self.chaty.setGeometry(QtCore.QRect(10, 160, 391, 381))
        self.chaty.setObjectName("chaty")
        self.send_text = QtWidgets.QLineEdit(self.centralwidget) #where to input texts
        self.send_text.setGeometry(QtCore.QRect(10, 550, 391, 51))
        self.send_text.setObjectName("send_text")
        self.send_button = QtWidgets.QPushButton(self.centralwidget) #button to send text
        self.send_button.setGeometry(QtCore.QRect(160, 610, 75, 23))
        self.send_button.setObjectName("send_button")
        loginButton.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginButton)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 22))
        self.menubar.setObjectName("menubar")
        loginButton.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginButton)
        self.statusbar.setObjectName("statusbar")
        loginButton.setStatusBar(self.statusbar)

        self.retranslateUi(loginButton)
        QtCore.QMetaObject.connectSlotsByName(loginButton)

    def retranslateUi(self, loginButton):
        _translate = QtCore.QCoreApplication.translate
        loginButton.setWindowTitle(_translate("loginButton", "MainWindow"))
        self.label.setText(_translate("loginButton", "NickName "))
        self.pushButton.setText(_translate("loginButton", "Login"))
        self.label_2.setText(_translate("loginButton", "Change Passworsd"))
        self.password_change_button.setText(_translate("loginButton", "Update"))
        self.send_button.setText(_translate("loginButton", "Send"))

