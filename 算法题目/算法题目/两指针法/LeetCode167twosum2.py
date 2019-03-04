#Author guo
class Solution:
    def twoSum(self, numbers, target):
        fast=0
        last=len(numbers)-1
        while (fast<last):
            if target<(numbers[last]+numbers[fast]):
                last=last-1
            elif target>(numbers[last]+numbers[fast]):
                fast=fast+1
            else:
                return fast+1,last+1
#前后两个指针，遍历
#当前后两个相同时，返回他们的index

