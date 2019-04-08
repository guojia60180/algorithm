#Author guo
class Solution:
    def majorityElement(self, nums):
       #对数组排序，最中间的数出现次数一定多于n/2

        #利用计数器来解决这个问题，当遍历到元素和统计元素不相等时
#使cnt--
        nums=sorted(nums)
        return nums[len(nums)//2]