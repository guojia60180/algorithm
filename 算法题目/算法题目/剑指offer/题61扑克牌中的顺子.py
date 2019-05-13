#Author guo
#首先数组排序
#统计排序后数组相邻数字之间空缺总数
#空缺综述小于或者等于0的个数，数组连续

# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if numbers==None or len(numbers)<=0:
            return False

        dic={'A':1,'J':11,'Q':12,'K':13}

        for i in range(len(numbers)):
            if numbers[i] in dic.keys():
                numbers[i]=dic[numbers[i]]

        numbers=sorted(numbers)
        numberofzero=0
        numberofgap=0

        #统计0个数
        i=0
        while i<len(numbers) and numbers[i]==0:
            numberofzero+=1
            i+=1

        #统计间隔

        small=numberofzero
        big=small+1
        while big<len(numbers):
            #对子
            if numbers[small]==numbers[big]:
                return False

            numberofgap+=numbers[big]-numbers[small]-1
            small=big
            big+=1
        return False if numberofgap!=numberofzero else True