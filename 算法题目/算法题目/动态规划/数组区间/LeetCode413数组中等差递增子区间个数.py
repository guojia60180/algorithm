#Author guo
'''
dp[i]表示以A[i]为结尾的等差递增子区间的个数
如果3连是一个等差子区间，下一组也是等差递增子区间

'''
class Solution:
    def numberOfArithmeticSlices(self, A):
        if  A==None or len(A)==0:
            return 0

        n=len(A)
        dp=[0]*n
        for i in range(2,n):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1

        total=0
        for x in dp:

            total=total+x

        return total