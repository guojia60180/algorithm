#Author guo
class Solution:
    def nextGreaterElements(self, nums):
        n=len(nums)
        next=[-1]*n
        stack=[]

        for i in range(n*2):
            num=nums[i%n]
            while stack and nums[stack[-1]]<num:
                next[stack.pop()]=num

            if i<n:
                stack.append(i)


        return next
