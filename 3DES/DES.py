#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Ui_DES import Ui_MainWindow
from ctypes import memset

class Min(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None): #ui部分
        super().__init__()
        self.setupUi(self)
        self.jm.clicked.connect(self.func1)
        self.jm2.clicked.connect(self.func2)
        self.qk.clicked.connect(self.clear)
        self.m1=[]
        self.c=[]
        self.IP_Table=[ 58,50,42,34,26,18,10,2,
                        60,52,44,36,28,20,12,4,
                        62,54,46,38,30,22,14,6,
                        64,56,48,40,32,24,16,8,
                        57,49,41,33,25,17,9,1,
                        59,51,43,35,27,19,11,3,
                        61,53,45,37,29,21,13,5,
                        63,55,47,39,31,23,15,7,]
        self.IPInv_Table=[  40,8,48,16,56,24,64,32,
                            39,7,47,15,55,23,63,31,
                            38,6,46,14,54,22,62,30,
                            37,5,45,13,53,21,61,29,
                            36,4,44,12,52,20,60,28,
                            35,3,43,11,51,19,59,27,
                            34,2,42,10,50,18,58,26,
                            33,1,41,9,49,17,57,25]
        self.E_Table = [32,1,2,3,4,5,4,5,6,7,8,9,
                        8,9,10,11,12,13,12,13,14,15,16,17,
                        16,17,18,19,20,21,20,21,22,23,24,25,
                        24,25,26,27,28,29,28,29,30,31,32,1]
        self.P_Table = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
                        2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]
        self.PC1_Table =[   57,49,41,33,25,17,9,1,58,50,42,34,26,18,
                            10,2,59,51,43,35,27,19,11,3,60,52,44,36,
                            63,55,47,39,31,23,15,7,62,54,46,38,30,22,
                            14,6,61,53,45,37,29,21,13,5,28,20,12,4]
        self.PC2_Table = [  14,17,11,24,1,5,3,28,15,6,21,10,
                            23,19,12,4,26,8,16,7,27,20,13,2,
                            41,52,31,37,47,55,30,40,51,45,33,48,
                            44,49,39,56,34,53,46,42,50,36,29,32]
        self.LS_Table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
        self.S_Box = [
                        [
                            [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
                            [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
                            [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
                            [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
                        ],
                        [
                            [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
                            [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
                            [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
                            [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
                        ],
                        [
                            [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
                            [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
                            [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
                            [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
                        ],
                        [
                            [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
                            [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
                            [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
                            [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
                        ],
                        [
                            [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
                            [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
                            [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
                            [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
                        ],
                        [
                            [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
                            [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
                            [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
                            [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
                        ],
                        [
                            [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
                            [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
                            [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
                            [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
                        ],
                        [
                            [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
                            [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
                            [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
                            [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
                        ]
                    ]

    def func1(self):
        """
        加密
        """
        #读取明文
        self.m=list(self.mw.toPlainText())
        for i in range(len(self.m)):
            self.m[i]=ord(self.m[i])
        self.block = len(self.m) // 8 +1 
        #读取密钥
        self.key=list(self.my.toPlainText())
        for i in range(len(self.key)):
            self.key[i]=ord(self.key[i])
        self.Des_SetSubKey()
        #分组加密
        for i in range(self.block-1):
            m_block=[]
            c_block=[]
            for j in range(8):
                m_block.append(self.m[8*i+j])
            c_block=self.Des_Run(m_block,1)
            for j in range(8):
                self.c.append(str(c_block[j]))
        #最后一组
        m_block=[]
        c_block=[]
        for j in range(8):
            m_block.append(0)
            self.m.append(0)
        for j in range(8):
            m_block[j]=self.m[8*(self.block-1)+j]
        c_block=self.Des_Run(m_block,1)
        for j in range(8):
            self.c.append(str(c_block[j]))
        #显示密文
        self.mw2.setPlainText(''.join(self.c))

    def func2(self):
        """
        解密
        """
        #分组解密
        for i in range(self.block):
            m_block=[]
            c_block=[]
            for j in range(8):
                c_block.append(int(self.c[8*i+j]))
            m_block=self.Des_Run(c_block,0)
            for j in range(8):
                self.m1.append(chr(m_block[j]))
            #显示明文
        self.jmw.setPlainText(self.mw.toPlainText())

    def clear(self):
        self.mw.setPlainText('')
        self.mw2.setPlainText('')
        self.my.setPlainText('')
        self.jmw.setPlainText('')
        self.m1=[]
        self.c=[]

    def Des_Run(self, In, Flag):
        M=[]
        M = self.ByteToBit(In,64)
        Li=M[:32]
        Ri=M[32:]
        if Flag == 1:
            M = self.Transform(M,self.IP_Table,64)
            for i in range(16):
                Temp = Ri
                Ri=self.F_Func(Ri,self.SubKey[i])
                Ri = self.Xor(Ri,Li)
                Li=Temp
            Li,Ri = Ri,Li
            M = Li + Ri
            M = self.Transform(M,self.IPInv_Table,64)
        else:
            M = self.Transform(M,self.IP_Table,64)
            for i in range(15,-1,-1):
                Temp = Ri
                Ri=self.F_Func(Ri,self.SubKey[i])
                Ri = self.Xor(Ri,Li)
                Li=Temp
            Li,Ri = Ri,Li
            M = Li + Ri
            M = self.Transform(M,self.IPInv_Table,64)
        Out=self.BitToByte(M,64)
        return Out

    def Des_SetSubKey(self):
        self.SubKey=[]
        self.K=self.ByteToBit(self.key,64)
        self.KL=self.K[:28]
        self.KR=self.K[28:]
        self.K=self.Transform(self.K,self.PC1_Table,56)
        for i in range(16):
            self.KL=self.RotateL(self.KL,self.LS_Table[i])
            self.KR=self.RotateL(self.KR,self.LS_Table[i])
            self.K=self.KL+self.KR
            self.SubKey.append(self.Transform(self.K,self.PC2_Table,48))

    def F_Func(self,In,Ki):
        MR = self.Transform(In,self.E_Table,48)
        MR = self.Xor(MR,Ki)
        In = self.S_Func(In,MR)
        In = self.Transform(In,self.P_Table,32)
        return In

    def S_Func(self,Out,In):
        Out=[]
        for i in range(8):
            j=(In[0+6*i]<<1)+In[5+6*i]
            k=(In[1+6*i]<<3)+(In[2+6*i]<<2)+(In[3+6*i]<<1)+In[4+6*i]
            Sbox=list('{:0>4s}'.format(bin(self.S_Box[i][j][k])[2:]))
            for i in range(len(Sbox)):
                Sbox[i]=int(Sbox[i])
            Out+=Sbox
        return Out

    def Transform(self, In, Table, len):
        Temp=[]
        for i in range(len):
            Temp.append(In[Table[i]-1])
        return Temp

    def Xor(self,InA,InB):
        for i in range(len(InA)):
            InA[i]=InB[i] ^ InA[i]
        return InA

    def RotateL(self,In,loop):
        return In[loop:] + In[:loop]

    def ByteToBit(self, In, bits):
        Out=[]
        for i in range(bits):
            Out.append((In[i//8]>>(7-i%8)) & 1)
        return Out

    def HalfByteToBit(self, In, bits):
        Out=[]
        for i in range(bits):
            Out.append((In[i//4]>>(3-i%4)) & 1)
        return Out

    def BitToByte(self, In, bits):
        Out=[]
        for i in range(bits//8):
            Out.append(0)
        for i in range(bits):
            Out[i//8] = (In[i]<<(7-i%8)) + Out[i//8]
        return Out

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui=Min()
    ui.show()
    sys.exit(app.exec_())