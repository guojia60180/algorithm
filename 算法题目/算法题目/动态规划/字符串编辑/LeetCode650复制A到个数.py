#Author guo
import math
class Solution:
    def minSteps(self, n):
        if n==1:
            return 0
        for i in range(2,math.sqrt(n)+1):
            if n%i==0:
                return i+self.minSteps(n/i)

        return n

    def minSteps(self,n):
        dp=[0]*(n+1)
        h=int(math.sqrt(n))

        for i in range(2,n+1):
            dp[i]=i
            for j in range(2,h+1):
                if i%j==0:
                    dp[i]=dp[j]+dp[i/j]
                    break

        return dp[n]