#Author guo
#找数组中最小数字，其中数组不是顺序的
class Solution:
    def findMin(self, nums) :
        l,r=0,len(nums)-1

        while l<r:
            mid=(l+r)//2
            if nums[mid]<=nums[r]:
                r=mid
            else:
                l=mid+1

        return nums[l]