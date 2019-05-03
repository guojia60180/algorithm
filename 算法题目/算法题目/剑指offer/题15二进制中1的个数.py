#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n<0:
            n=n&0xffffffff
        while n:
            count += 1
            n = (n - 1) & n

        return count
    def Numberof2(self,n):
        if n<0:
            s=bin(n&0xffffffff)
        else:
            s=bin(n)

        return s.count('1')

    #判断是否是2的整次数幂
    def powerof2(self,n):
        if n&(n-1)==0:
            return True
        else:
            return False


    #判断两个数二进制表示有多少位不一样
    def andOr(self,m,n):
        diff=m^n
        count=0
        while diff:
            count+=1
            diff=diff&(diff-1)#逐级的置0

        return count


