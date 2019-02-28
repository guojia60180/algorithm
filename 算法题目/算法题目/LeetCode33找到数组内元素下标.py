#Author guo
class Solution:
    # def search(self, nums, target):
    #     if target in nums:
    #         return nums.index(target)
    #     else:
    #         return -1

#二分查找

    def search(self,nums,target):
        if not nums:
            return -1

        left=0
        right=len(nums)-1

        while left<right:
            mid=(left+right)/2
            if target==nums[mid]:
                return mid
            if nums[left]<nums[mid]:
                if nums[left]<target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1

            else:
                if nums[mid]<target<nums[right]:
                    left=mid+1
                else:
                    right=mid-1

        return -1
