#Author guo
import collections
class Solution:
    def findTargetSumWays(self, nums, S):
        l=len(nums)
        dp=[collections.defaultdict(int) for _ in range(l+1)]
        dp[0][0]=1
        for i,num in enumerate (nums):
            for sum,cnt in dp[i].items():
                dp[i+1][sum+num]+=cnt
                dp[i+1][sum-num]+=cnt

        return dp[l][S]