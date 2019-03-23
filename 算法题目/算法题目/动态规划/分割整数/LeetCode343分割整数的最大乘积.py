#Author guo
class Solution:
    def integerBreak(self, n):
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i]=max(dp[i],max(j*dp[i-j],j*(i-j)))


        return dp[n]

'''
class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2: return 1
        if n == 3: return 2
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n
'''