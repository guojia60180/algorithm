#Author guo
#两个背包问题
class Solution:
    def findMaxForm(self, strs, m, n) :
        dp=[[0 for _ in range(n+1)]for _ in range(m+1)]
        for str in strs:
            zeros,ones=0,0
            for char in str:
                if char=='0':
                    zeros+=1
                elif char=='1':
                    ones+=1

            for i in range(m,zeros-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zeros][j-ones]+1)
        return dp[m][n]