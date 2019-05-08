#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss)==0:
            return []
        if len(ss)==1:
            return list(ss)

        charlist=list(ss)
        charlist=sorted(charlist)
        res=[]
        for i in range(len(charlist)):
            if i>0 and charlist[i]==charlist[i-1]:
                continue
            temp=self.Permutation(''.join(charlist[:i])+''.join(charlist[i+1:]))
            for j in temp:
                res.append(charlist[i]+j)



        return res

 # 扩展习题, 生成字符的所有组合
    # 比如输入abc, 则他们的组合有['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'], ab和ba属于不同的排列, 但属于同一个组合
    def group(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            pStr.append(charList[i])
            if i > 0 and charList[i] == charList[i - 1]:
                continue#跳出本次循环 break跳出整个循环
            temp = self.group(''.join(charList[i + 1:]))
            for j in temp:
                pStr.append(charList[i] + j)
            pStr = list(set(pStr))
            pStr.sort()
        return pStr

ss = 'acb'
S = Solution()
# print(S.Permutation(ss))
print(S.group(ss))