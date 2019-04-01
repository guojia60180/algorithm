#Author guo
'''
buy1=max(buy1,−prices[i])

sell1=max(sell1,buy1+prices[i]) sell1 = max(sell1, buy1 + prices[i])sell1=max(sell1,buy1+prices[i])

buy2=max(buy2,sell1−prices[i]) buy2 = max(buy2, sell1 - prices[i])buy2=max(buy2,sell1−prices[i])

sell2=max(sell2,buy2+prices[i]) sell2 = max(sell2, buy2 + prices[i])sell2=max(sell2,buy2+prices[i])

'''
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        buy1=-prices[0]
        sell1=0
        buy2=-prices[0]
        sell2=0

        for i in range(1,len(prices)):
            buy1=max(buy1,-prices[i])
            sell1=max(sell1,buy1+prices[i])
            buy2=max(buy2,sell1-prices[i])
            sell2=max(sell2,buy2+prices[i])

        return max(sell2,sell1)