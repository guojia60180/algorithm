#Author guo
#数组的度为元素出现的最高频率
#要求找到一个最小的子数组，子数组的度和原数组一样
import collections
class Solution:
    def findShortestSubArray(self, nums):
        nums_set=set(nums)
        if len(nums)==len(nums_set):
            return 1
        nums_dic={num:nums.count(num) for num in nums_set}
        degree=max(nums_dic.values())#建立一个Counter找到最大重复值度
        most_numbers=[num for num in nums_set if nums_dic[num]==degree]
        scale=1000000
        for most_number in most_numbers:
            appear=[i for i,num in enumerate(nums) if num==most_number]
            appear_scale=max(appear)-min(appear)+1
            if appear_scale<scale:
                scale=appear_scale

        return scale