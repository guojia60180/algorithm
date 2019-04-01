#Author guo
#只进行一次交易
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        min=prices[0]
        maxp=0
        for i in range(1,len(prices)):
            if min>prices[i]:
                min=prices[i]
            else:
                maxp=max(maxp,prices[i]-min)#在最小处买到
                #找到与后面的差距最大值即可，更新maxp

        return maxp