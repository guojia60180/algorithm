#Author guo

class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0

        cursum=maxsum=nums[0]
        for num in nums[1:]:
            cursum=max(num,cursum+num)
            maxsum=max(cursum,maxsum)

        return maxsum
