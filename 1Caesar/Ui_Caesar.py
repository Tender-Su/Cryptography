# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\OneDrive\我Python牛皮\密码学实验\Caesar.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mw = QtWidgets.QTextEdit(self.centralwidget)
        self.mw.setGeometry(QtCore.QRect(60, 30, 381, 131))
        self.mw.setObjectName("mw")
        self.mw2 = QtWidgets.QTextEdit(self.centralwidget)
        self.mw2.setGeometry(QtCore.QRect(60, 190, 381, 131))
        self.mw2.setObjectName("mw2")
        self.my = QtWidgets.QTextEdit(self.centralwidget)
        self.my.setGeometry(QtCore.QRect(60, 340, 121, 51))
        self.my.setObjectName("my")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 41, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 350, 54, 12))
        self.label_3.setObjectName("label_3")
        self.jm = QtWidgets.QRadioButton(self.centralwidget)
        self.jm.setGeometry(QtCore.QRect(470, 30, 89, 16))
        self.jm.setObjectName("jm")
        self.jm2 = QtWidgets.QRadioButton(self.centralwidget)
        self.jm2.setGeometry(QtCore.QRect(470, 70, 89, 16))
        self.jm2.setObjectName("jm2")
        self.jjm = QtWidgets.QPushButton(self.centralwidget)
        self.jjm.setGeometry(QtCore.QRect(470, 190, 75, 23))
        self.jjm.setObjectName("jjm")
        self.qk = QtWidgets.QPushButton(self.centralwidget)
        self.qk.setGeometry(QtCore.QRect(470, 230, 75, 23))
        self.qk.setObjectName("qk")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caesar"))
        self.label.setText(_translate("MainWindow", "明文"))
        self.label_2.setText(_translate("MainWindow", "密文"))
        self.label_3.setText(_translate("MainWindow", "密钥"))
        self.jm.setText(_translate("MainWindow", "加密"))
        self.jm2.setText(_translate("MainWindow", "解密"))
        self.jjm.setText(_translate("MainWindow", "加/解密"))
        self.qk.setText(_translate("MainWindow", "清空"))
