#Author guo
class Solution:
    def partitionLabels(self, S):
        res=[]
        last={}

        for i in range(len(S)-1,-1,-1):
            if S[i] not in last:
                last[S[i]]=i#创建字典，字符串中字符与index对应

        i=0
        span=0
        while i<len(S):
            j=last[S[i]]
            span=1
            while i!=j:
                i=i+1
                span+=1
                h=max(j,last[S[i]])
            res.append(span)
            i=i+1

        return res
