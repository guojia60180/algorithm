#Author guo
#对于数字 6(110)，
# 它可以看成是 4(100) 再加一个 2(10)，
# 因此 dp[i] = dp[i&(i-1)] + 1;
class Solution:
    #暴力
    def countBits(self, num):
        res=[]
        for i in range(num+1):
            res.append(bin(i).count('1'))

        return res

    #通过观察前10个数的二进制，可以发现
        # ：[2-3]中1的个数是[0-1]中个数对应加一；
        # [4-7]是[0-3]对应加一；
        # [8-15]是[0-7]对应加一；

        # 本质上，是将最高位的1变成0得到对应的较小的数
    #右边限是2倍+1的关系
    def countBits1(self, num):
        dp=[0]
        i=0
        while True:
            for j in range(1<<i,1<<(i+1)):
                if j>num:
                    return dp
                dp.append(1+dp[j-(1<<i)])
            i+=1

        return dp