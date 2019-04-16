#Author guo
class Solution:
    def isAnagram(self, s, t):
        #hash映射字符与出现次数，比较两个字符串出现字符数量是否相同
        if len(s)!=len(t):
            return False

        alpha={}
        beta={}
        for c in s:
            alpha[c]=alpha.get(c,0)+1

        for c in t:
            beta[c]=beta.get(c,0)+1

        return alpha==beta

    #构建了一个collection.Counter来进行计算

    #利用sorted来判断

class Solution:
    def isAnagram2(self, s, t):
        return sorted(s)==sorted(t)