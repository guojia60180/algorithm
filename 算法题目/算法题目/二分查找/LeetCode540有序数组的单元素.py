#Author guo
import collections
class Solution:
    def singleNonDuplicate(self, nums):

        l,h=0,len(nums)-1
        while(l<h):
            m=(l+h)//2
            if m%2==1:
                m=m-1#使其在偶数位查找
            if nums[m]==nums[m+1]:
                l=m+2#增加两位
            else:
                h=m

        return nums[l]




