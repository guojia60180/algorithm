#Author guo
# -*- coding:utf-8 -*-
import collections
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return 0
        dic=collections.Counter(s)
        for i,char in enumerate(s):
            if dic[char]==1:
                return i

def searFisrt(str):
    #定义一个数据字典
    dic={}
    for i in range(len(str)):
        if str[i] in dic:
            dic[str[i]]+=1
        else:
            dic[str[i]]=1
    for i in range(len(str)):
         if dic[str[i]]==1:
             return str[i]
str='asasc'
print(searFisrt(str))