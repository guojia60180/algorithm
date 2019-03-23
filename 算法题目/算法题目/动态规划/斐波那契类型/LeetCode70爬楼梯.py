#Author guo
'''
动态规划将原问题拆成多个子问题进行求解
动态规划保存了子问题的解，避免重复计算


N阶楼梯
每次可以上两个或者一个 求上楼梯的方法

定义一个数组dp存储方法数，dp[i]表示走到第i个楼梯的方法数目
第i个楼梯可以从第i-1和i-2个楼梯一步到达
走到第i个楼梯的方法树为走到第i-1和第i-2个楼梯的方法数之和
'''

class Solution:
    def climbStairs(self, n):
        if n<=2:
            return n
        pre1=1
        pre2=2
        for i in range(2,n):
            cur=pre1+pre2
            pre1=pre2
            pre2=cur

        return pre2