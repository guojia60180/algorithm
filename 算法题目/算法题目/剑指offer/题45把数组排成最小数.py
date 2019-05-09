#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''

        num=[str(i) for i in numbers]
        for i in range(len(num)):
            for j in range(i+1,len(numbers)):
                list1=[num[i],num[j]]
                list2=[num[j],num[i]]

                if ''.join(list1)>''.join(list2):#字符串比较，就不用了管数字了
                    num[i],num[j]=num[j],num[i]

        res=int(''.join(num))
        return res