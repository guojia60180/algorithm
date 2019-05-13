#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return sum(list(range(0,n+1)))

    def Sum_Solution1(self, n):
        return n and n+self.Sum_Solution1(n-1)#利用逻辑与的方式来终止递归

    #def __add__(self, other):
        #return self.__mul__(other)
    #def __sub__(self, other):
        #return self.__div__(other)
    #重写操作符内建方法
    #直接调函数__mul__ __truediv__（python3用） （python2可以使用__div__）
    def Sum_Solution2(self, n):
        #n.__mul__(n-1)
        return  int((n+1).__mul__(n).__truediv__(2))

s=Solution()
print(s.Sum_Solution2(1))