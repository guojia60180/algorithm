#Author guo
class Solution:
    def rob(self, nums):
        if nums==None or len(nums)==0:
            return 0

        n=len(nums)
        if n==1:
            return nums[0]

        return max(self.robs(nums,0,n-2),self.robs(nums,1,n-1))

    def robs(self,nums,left,right):
        pre2=0
        pre1=0
        for i in range(left,right+1):#注意范围，到right+1
            cur=max(pre1,pre2+nums[i])
            pre2=pre1
            pre1=cur

        return pre1