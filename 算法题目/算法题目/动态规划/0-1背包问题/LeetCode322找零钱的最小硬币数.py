#Author guo
'''
构建一个长度是amount + 1的dp数组，其含义是能够成面额从0到amount + 1需要使用的最少硬币数量

dp更新的策略是从coin面额到amount+1的面额依次向后查找
看这个位置能不能用更少的硬币组成（即使用面额是i - coin的需要硬币数量+1)
'''
class Solution:
    def coinChange(self, coins, amount):
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin,amount+1):
                if dp[i-coin]!=float('inf'):
                    dp[i]=min(dp[i],dp[i-coin]+1)

        return -1 if dp[amount]==float('inf') else dp[amount]