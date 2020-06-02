#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Ui_RSA import Ui_MainWindow
import random
import secrets

class Min(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None): #ui部分
        super().__init__()
        self.setupUi(self)
        self.sj.clicked.connect(self.func1)
        self.jm.clicked.connect(self.func2)
        self.jm2.clicked.connect(self.func3)
        self.m1=[]
        self.c=[]

    def func1(self):
        """
        生成随机密钥
        """
        self.nump=self.GenPrime(16)
        self.numq=self.GenPrime(16) 
        self.numN=self.nump*self.numq 
        self.numPhiN=(self.nump-1)*(self.numq-1)
        self.nume=self.GenE(self.numPhiN)
        self.numd=self.Inverse(self.nume,self.numPhiN)
        #显示
        self.P.setPlainText(str(self.nump))
        self.Q.setPlainText(str(self.numq))
        self.N.setPlainText(str(self.numN))
        self.e.setPlainText(str(self.nume))
        self.d.setPlainText(str(self.numd))
        

    def func2(self):
        """
        加密
        """
        self.m=list(self.mw.toPlainText())
        for ms in self.m:
            self.c.append(str(self.fast_power(ord(ms) , self.nume, self.numN)))
        self.mw2.setPlainText(''.join(self.c))

    def func3(self):
        """
        解密
        """
        for cs in self.c:
            cs=int(cs)
            self.m1.append(chr(self.fast_power(cs , self.numd, self.numN)))
        self.jmw.setPlainText(''.join(self.m1))

    def Inverse(self, e, N):

        r1 = e
        r2 = N
        s1 = 1
        s2 = 0
        while (1):
            if (r1 == 0):
                return 0
            if (r1 == 1):
                d = s1
                return d
            q = r1 // r2
            s = self.Sub2Mod(s1, (q* s2% N), N) 
            r = r1-(q* r2)
            r1 = r2
            s1 = s2
            s2 = s
            r2 = r

    def Sub2Mod(self, a, b, n):

        while (a - b < 0):
            a += n
        return (a - b)

    def GenE(self, PhiN):
        e = random.randint(0,PhiN)
        g = self.GCD(PhiN,e)
        while g != 1:
            e = random.randint(0,PhiN)
            g = self.GCD(PhiN,e)
        return e


    def GCD(self,a,b):
        if a%b == 0:
            return b
        else :
            return self.GCD(b,a%b)

    def fast_power(self, base, power, n):
        """
        快速模幂运算
        """
        result = 1
        tmp = base
        while power > 0:
            if power&1 == 1:
                result = (result * tmp) % n
            tmp = (tmp * tmp) % n 
            power = power>>1
        return result

    def Miller_Rabin(self, n, iter_num):
        """
        Miller_Rabin素性检测
        """
        # 2 is prime
        if n == 2:
            return True
        # if n is even or less than 2, then n is not a prime
        a=n&1
        if n&1 == 0 or n<2:
            return False
        # n-1 = (2^s)m
        m,s = n - 1,0
        while m&1==0:
            m = m>>1
            s += 1
        # M-R test
        for _ in range(iter_num):
            b = self.fast_power(random.randint(2,n-1), m, n)
            if b==1 or b== n-1:
                continue
            for __ in range(s-1):
                b = self.fast_power(b, 2, n)
                if b == n-1:
                    break
            else:
                return False
        return True

    def RandOdd(self, byte):
        """
        生成若干bytes的随机奇数
        """
        byte*=8
        num=secrets.randbits(byte)
        if num&1 == 0:
            num+=1
        return num

    def GenPrime(self, byte):
        """
        生成若干bytes的随机素数
        """
        res=self.RandOdd(byte)
        while self.Miller_Rabin(res,20) == False:
            res=self.RandOdd(byte)
        return res

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui=Min()
    ui.show()
    sys.exit(app.exec_())