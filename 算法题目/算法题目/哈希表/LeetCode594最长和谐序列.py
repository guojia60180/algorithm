#Author guo
import collections
#和谐序列中最大和最小数差1，序列中的元素不一定连续
class Solution:
    def findLHS(self, nums):
        #具体在python中利用计数来进行计算
        counter=collections.Counter(nums)#生成一个字典
        num_set=set(nums)
        longest=0
        for num in num_set:
            if num+1 in counter:
                longest=max(longest,counter[num]+counter[num+1])
        return longest