#Author guo
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if s==None:
            return False
        alist=[w.lower() for w in s]#全部先小写转换成字符串列表

        if 'e' in alist:#如果e在alist里时
            indexE=alist.index('e')#找到e的index
            front=alist[:indexE]#分为两部分
            back=alist[indexE+1:]

            if '.' in back or len(back)==0:
                return False

            frontconfused=self.scanDigit(front)#判断前面一部分是否可以过检测
            backconfused=self.scanDigit(back)
            return frontconfused and backconfused
        else:
            Numconfused=self.scanDigit(alist)#如果不包含e，就只有数字部分和小数点部分
            return Numconfused

    def scanDigit(self,alist):
        dotNum=0
        allowedVal=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e']
        for i in range(len(alist)):
            if alist[i] not in allowedVal:#判断错误输入字符
                return False
            if alist[i]=='.':#统计.数量，超过一个返回false
                dotNum+=1

            if alist[i] in '+-' and i!=0:#判断在+-中，而且位置是不是在首尾，只有在第一位才可以认为可以检测通过
                #由于从e两边分离，因此可以这样使用
                return False
        if dotNum>1:
            return False#点的个数大于1时，错
        return True