#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Ui_RC4 import Ui_MainWindow

class Min(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None): #ui部分
        super().__init__()
        self.setupUi(self)
        self.jm.clicked.connect(self.func1)
        self.jm2.clicked.connect(self.func2)
        self.qk.clicked.connect(self.clear)
        self.m1=[]
        self.c=[]
        self.kstr=[]
    def start(self):
        j=0
        #读取密钥
        self.key=list(self.my.toPlainText())
        #读取明文
        self.m=list(self.mw.toPlainText())
        #初始化S盒
        self.S=[i for i in range(256)]
        #利用密钥打乱S盒
        for i in range(256):

            j=(j+self.S[i]+ord(self.key[i%len(self.key)]))%256
            self.S[i],self.S[j]=self.S[j],self.S[i]
        #生成密钥流
        i=0
        j=0
        for k in range(len(self.m)):
            i=(i+1)%256
            j=(j+self.S[i])%256
            self.S[i],self.S[j]=self.S[j],self.S[i]
            self.kstr.append(self.S[(self.S[i]+self.S[j])%256])
            
    def func1(self):
        self.start()
        #加密
        for i in range(len(self.m)):
            self.c.append(chr(int(self.kstr[i])^ord(self.m[i])))
        #显示密文
        self.mw2.setPlainText(''.join(self.c))
        #显示密钥流
        kstr=[str(i) for i in self.kstr]
        self.myl.setPlainText(''.join(kstr))
        
    def func2(self):
        self.start()
        #解密
        for i in range(len(self.m)):
            self.m1.append(chr(int(self.kstr[i])^ord(self.c[i])))
        #显示明文
        self.jmw.setPlainText(''.join(self.m1))
        #显示密钥流
        kstr=[str(i) for i in self.kstr]
        self.myl.setPlainText(''.join(kstr))
        
    def clear(self):
        self.mw.setPlainText('')
        self.mw2.setPlainText('')
        self.my.setPlainText('')
        self.myl.setPlainText('')
        self.jmw.setPlainText('')
        self.m1=[]
        self.c=[]
        self.kstr=[]

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui=Min()
    ui.show()
    sys.exit(app.exec_())