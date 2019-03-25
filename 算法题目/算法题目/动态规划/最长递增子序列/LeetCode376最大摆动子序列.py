#Author guo
class Solution:
    def wiggleMaxLength(self, nums):
        n=len(nums)
        if n<=1:
            return n
        inc=1
        dec=1
        for x in range(1,n):
            if nums[x]>nums[x-1]:
                inc=dec+1

            elif nums[x]<nums[x-1]:
                dec=inc+1

        return max(inc,dec)
