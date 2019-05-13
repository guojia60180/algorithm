#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if A==None or len(A)<=0:
            return
        length=len(A)
        alist=[1]*length
        for i in range(1,length):
            alist[i]=alist[i-1]*A[i-1]

        temp=1
        for i in range(length-2,-1,-1):
            temp=temp*A[i+1]
            alist[i]*=temp

        return alist

test=[1,2,3,4]
s=Solution()
print(s.multiply(test))