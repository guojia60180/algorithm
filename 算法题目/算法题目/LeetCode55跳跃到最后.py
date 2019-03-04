#Author guo
class Solution(object):
    def canJump(self, nums):
        index=reach=0

        if len(nums)<=1:
            return True

        while index<len(nums):
            if reach<index:
                return False#如果该点的index值+数值还是小于最后一个

            reach=max(reach,nums[index]+index)
            index=index+1

        return True