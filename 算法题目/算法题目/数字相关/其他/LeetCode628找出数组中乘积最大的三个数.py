#Author guo
class Solution:
    def maximumProduct(self, nums):
        #唯一需要注意的是存在负数。所以结果应为“最大三个数的乘积”与“最大数与最小两个数的乘积”中较大的那个
        nums=sorted(nums)
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])
