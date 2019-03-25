#Author guo
class Solution:
    def findLongestChain(self, pairs):
        if pairs==None or len(pairs)==0:
            return 0

        pairs.sort(key=lambda x:x[1])
        curr=float('-inf')
        ans=0
        for x,y in pairs:
            if curr<x:
                curr=y
                ans=ans+1

        return ans