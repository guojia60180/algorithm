#Author guo
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        sell=[0]*len(prices)#手里没有股票的收益
        hold=[0]*len(prices)#手里有股票的收益
        hold[0]=-prices[0]
        for i in range(1,len(prices)):
            sell[i]=max(sell[i-1],hold[i-1]+prices[i])#前一天的卖出收益和保持+价格
            hold[i]=max(hold[i-1],(sell[i-2] if i>=2 else 0)-prices[i])#前一天手里有的收益，前两天卖出收益-今天的价格
        return sell[-1]