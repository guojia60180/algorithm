#Author guo
class NumArray:
    def __init__(self, nums):
        self.sums=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.sums[i+1]=self.sums[i]+nums[i]
    def sumRange(self, i, j):
        return self.sums[j+1]-self.sums[i]
