# 杭州电子科技大学 密码学课程设计

**实验列表**

- [x] [Lab1-Caesar密码]
- [x] [Lab2-RC4流密码]
- [x] [Lab3-DES分组密码]
- [x] [Lab4-SM4分组密码]
- [x] [Lab5-RSA非对称加密]

## 说明

部分老师可能会严格要求用C++的MFC做

我的老师允许使用python, 因此用python和pyqt5做了一次重构

## 优势

由于python的简洁性

###### Caesar密码和RC4流密码 重构后代码量少, 相对C++而言有少量优势

由于python原生支持超大整数的运算

##### RSA加密算法 重构后代码简洁, 运行速度快, 相对C++来说有巨大的优势

## 缺陷

由于SM4中涉及大量移位、异或、置换操作

###### SM4 的代码几乎复刻C++原版, 效率低下

由于DES涉及了大量对地址的直接操作

重构难度巨大, 即便经过了五小时的调试

### DES 分组密码的加解密过程依旧是错误的

已查明问题发生在方法`self.Des_Run()`当中

```python
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
```

其中十六轮的加密过程发生了错误

可以断言问题发生在第10, 11, 20, 21行的`self.F_Func()`函数与`self.Xor()`中

精力有限, 没能继续完成修改

期待各位大佬的帮助与修正

## 救救孩子

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

## 声明
本项目库用于存放杭州电子科技大学密码学实验课程设计相关代码文件，所有代码仅供各位同学学习参考使用。

如有任何对代码的问题请邮箱联系：453986082@qq.com