#Author guo
#滑动窗口的最大值
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size<=0:
            return []

        length=len(num)
        res=[]

        for i in range(length-size+1):
            res.append(max(num[i:i+size]))

        return res