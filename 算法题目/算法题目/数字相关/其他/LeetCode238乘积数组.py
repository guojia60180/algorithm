#Author guo
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        left = 1
        for i in range(1, n):
            left *= nums[i - 1]
            res[i] *= left

        right = 1
        for i in range(n - 2, -1, -1):
            right *= nums[i + 1]
            res[i] *= right

        return res
