#Author guo
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        # duplication=sorted(duplication)
        hash = []
        for x in numbers:
            if x not in hash:
                hash.append(x)
            else:
                duplication[0] = x
                return True
        if len(hash) == len(numbers):
            return False

