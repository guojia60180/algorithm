#Author guo
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max1=0
        cur=0
        for x in nums:
            cur=0 if x==0 else cur+1
            max1=max(max1,cur)

        return max1
