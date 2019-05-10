#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum<3:
            return []

        #seqsum=[i for i in range(1,tsum)]
        #print(seqsum)
        small=1
        big=2
        middle=(1+tsum)//2
        cursum=small+big
        #cursum=sum(seqsum[i] for i in range(small-1,big))
        res=[]
        while small<big:


            if tsum==cursum:
                res.append(list(range(small,big+1)))
                big+=1
                cursum+=big

            elif cursum>tsum:
                cursum-=small
                small+=1
            else:
                big+=1
                cursum+=big

        return res

s=Solution()
print(s.FindContinuousSequence(11))