#Author guo
#每次交易都需要一定费用

class Solution:
    def maxProfit(self, prices, fee):
        if not prices:
            return 0
        sell=[0]*len(prices)
        hold=[0]*len(prices)
        hold[0]=-prices[0]
        for i in range(1,len(prices)):
            sell[i]=max(sell[i-1],hold[i-1]+prices[i]-fee)
            hold[i]=max(hold[i-1],sell[i]-prices[i])

        return sell[-1]