#Author guo
class Solution(object):
    def romanToInt(self,s):
        dic= {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res=0
        left=0

        for v in s:
            if left<dic[v]:
                res=res-2*left#如果字母出现在前面
            res=res+dic[v]
            left=dic[v]

        return res
