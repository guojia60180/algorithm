#Author guo
class Solution:
    def removeDuplicates(self, nums):

        if not nums:
            return 0
        i = j = 0
        for i in range( len(nums)):

            if nums[i] != nums[i + 1]:
                nums[j] = nums[i]
                j = j + 1

        return j

#i,j两个指针，i块，j慢
#碰见相同的，i++
#碰见不同的j++
#最后数组去重