#Author guo
class Solution:
    def firstMissingPositive(self, nums):
        #把数值放到下标加1的位置，第一个与下标+1数值不同的就是最小的遗失的
        n=len(nums)
        #[3,4,-1,1]->[1,-1,3,4]
        for i in range(n):
            while nums[i]>0 and nums[i]<n:
                if nums[i]!=i+1 and nums[i]!=nums[nums[i]-1]:
                    nums[i],nums[nums[i]-1]=nums[nums[i]-1],nums[i]
        for i in range(n):
            if i+1 !=nums[i]:
                return i+1
        return n+1

    #利用了数组索引与对应关系来解决


