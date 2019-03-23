#Author guo
'''
不能抢劫临近的住户，因此如果抢劫了第i个，那么只能抢劫i-2或i-3
个住户
dp[i]=max(dp[i-1],dp[i-2]+nums[i])
'''
class Solution:
    def rob(self, nums):
        pre2=0
        pre1=0

        for i in range(len(nums)):
            cur=max(pre2+nums[i],pre1)
            pre2=pre1
            pre1=cur

        return pre1
