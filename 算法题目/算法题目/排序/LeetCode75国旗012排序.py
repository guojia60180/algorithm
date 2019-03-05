#Author guo
class Solution:
    def sortColors(self, nums):
        l,r=0,len(nums)-1
        if l<r:
            pivot=self.pat(nums)
            self.sortColors(l,pivot-1)
            self.sortColors(pivot+1,r)
    def pat(self,nums):
        l,r=0,len(nums)-1
        pivot=nums[l]
        while l<r:
            while l<r and pivot<=nums[r]:
                r=r-1
            nums[l]=nums[r]
            while l<r and pivot>=nums[l]:
                l=l+1
            nums[r]=nums[l]
        nums[l]=pivot

        return l



