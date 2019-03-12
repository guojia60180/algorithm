#Author guo
class Solution:
    def diffWaysToCompute(self, input):
        res=[]
        N=len(input)
        for i in range(N):
            if input[i]=='+' or input[i]=='-' or input[i]=='*':
            #每遇到一个+-&号的时候，把前面和后面分两段
                lefts=self.diffWaysToCompute(input[:i])
                rights=self.diffWaysToCompute(input[i+1:])
                for left in lefts:
                    for right in rights:
                        if input[i]=='+':
                            res.append(left+right)
                        if input[i]=='-':
                            res.append(left-right)
                        if input[i]=='*':
                            res.append(left*right)
        if not res:
            res.append(input)
        return res