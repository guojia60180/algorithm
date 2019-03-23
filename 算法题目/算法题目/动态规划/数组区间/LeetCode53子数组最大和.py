#Author guo
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0

        cursum = maxsum = nums[0]
        for num in nums[1:]:
            cursum = max(num, cursum + num)  # 当前的和，迭代开始的数字，求最大值
            maxsum = max(cursum, maxsum)  # 总和 和当前和取最大
            # 穷搜的方式

        return maxsum