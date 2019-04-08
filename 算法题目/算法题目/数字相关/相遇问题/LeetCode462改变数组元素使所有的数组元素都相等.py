#Author guo
#典型的相遇问题，移动距离最小值是把元素移动到中位数
class Solution:
    def minMoves2(self, nums):
        nums=sorted(nums)
        move=0
        l=0
        h=len(nums)-1
        while l<=h:
            move+=nums[h]-nums[l]
            l+=1
            h-=1


        return move


#先进行排序

