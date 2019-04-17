#Author guo
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range (len(nums)):
            if nums[i]==0:
                index=i+1
                while index<len(nums) and nums[index]==0:
                    index+=1
                if index<len(nums):
                    nums[i]=nums[index]
                    nums[index]=0
    def moveZeroes2(self, nums):
        #这种方法考虑的是有的情况，当当前位置有非0时，把索引和当前值对应
        #最后判断point值和数组长度进行补0
        point=0
        for i in range(len(nums)):
            if nums[i]:
                nums[point]=nums[i]
                point+=1
        while point<len(nums):
            nums[point]=0
            point+=1