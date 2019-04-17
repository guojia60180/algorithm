#Author guo
class Solution:
    def findDuplicate(self, nums):
        #找出数组中重复值
        #利用链表成环
        slow=nums[0]
        fast=nums[nums[0]]
        while slow!=fast:
            fast=nums[nums[fast]]
            slow=nums[slow]
        fast=0
        while slow!=fast:
            fast=nums[fast]
            slow=nums[slow]
        return fast
    '''
    解法很奇妙
    因为有重复数字，指针会因为这个重复数字反复的经过某一条路径
    
    '''
    def findDuplicate2(self,nums):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            count=0
            for i in range(len(nums)):
                if nums[i]<=mid:
                    count+=1
            if count>mid:
                right=mid-1
            else:
                left=mid+1

        return left

    '''
    思路是我们在[1,N]范围内先求出mid，
    再统计小于等于mid的数字个数count，
    如果count<=mid，说明重复数字在[mid+1,N]中，
    否则在[1,mid)中'''
