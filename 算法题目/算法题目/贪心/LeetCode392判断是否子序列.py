#Author guo
class Solution:
    def isSubsequence(self, s, t):



        #两个指针，分别向后遍历寻找
        si,ti=0,0
        while si<len(s) and ti<len(t):
            if t[ti]==s[si]:#如果在t中能找到s中的元素
                si+=1
            ti+=1
        return si==len(s)