#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n<1 or m<1:
            return
        last=0
        lastlisr=[]
        for i in range(2,n+1):
            last=(last+m)%i
            lastlisr.append(last)
        return last
