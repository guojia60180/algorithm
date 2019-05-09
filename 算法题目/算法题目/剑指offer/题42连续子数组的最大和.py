#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return
        cursum=0
        maxsum=array[0]

        for i in range(len(array)):
            if cursum<=0:
                cursum=array[i]

            else:
                cursum+=array[i]

            if cursum>maxsum:
                maxsum=cursum

        return maxsum

    def FindGreatestSumOfSubArray2(self, array):
        if array==None:
            return 0
        dp=[0]*len(array)
        #dp[0]=array[0]
        for i in range(len(array)):
            if i==0 or dp[i-1]<=0:
                dp[i]=array[i]
            else:
                dp[i]=dp[i-1]+array[i]

        return max(dp)