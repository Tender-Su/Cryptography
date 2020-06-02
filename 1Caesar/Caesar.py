#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Ui_Caesar import Ui_MainWindow

class Min(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None): #ui部分
        super().__init__()
        self.setupUi(self)
        self.jjm.clicked.connect(self.func)
        self.qk.clicked.connect(self.clear)

    def func(self):
        key=0
        message=list(self.mw.toPlainText())
        cipher=message

        if self.jm.isChecked():
            key=int(self.my.toPlainText())
        elif self.jm2.isChecked():
            key=26-int(self.my.toPlainText())
        for i in range(len(message)):
            if ord(message[i]) + key > 122:
                cipher[i] = chr(ord(message[i]) - 26 + key)
            else:
                cipher[i] = chr(ord(message[i]) + key)
        self.mw2.setPlainText(''.join(cipher))

    def clear(self):
        self.mw.setPlainText('')
        self.mw2.setPlainText('')
        self.my.setPlainText('')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui=Min()
    ui.show()
    sys.exit(app.exec_())