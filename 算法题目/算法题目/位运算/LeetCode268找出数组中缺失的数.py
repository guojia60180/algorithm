#Author guo
class Solution:
    #数组元素在0-n之间，有一个数是缺失的，找缺失的数
    def missingNumber(self, nums):
        ret=0
        for i in range(len(nums)):
            ret=ret^i^nums[i]
        #a^0=a a^b^a=b
        #最初设置返回值res是nums的长度，目标值i^现有值nums[i]，
        # 那么如果i和nums[i]是相同的，异或的结果就是0，
        # 再让res^该结果，那么res仍等于res，
        # 这样说明i这个数是存在的，也就是说所有相同的数都被变成了0，
        # 剩下的就是缺失的数
        return ret^len(nums)

    def missingNumber1(self,nums):
        temp_sum=len(nums)*(len(nums)+1)//2
        t_sum=sum(nums)
        return temp_sum-t_sum

    def missingNumber2(self,nums):
        nums.sort()
        i=0
        while i<len(nums):
            if nums[i]!=i:
                return i
            else:
                i+=1
        return i#循环一遍数组，看是否等于

