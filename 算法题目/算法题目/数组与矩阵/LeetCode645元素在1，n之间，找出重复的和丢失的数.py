#Author guo
class Solution:
    def findErrorNums(self, nums):
        '''
        先对数组进行排序，这种方法时间复杂度NlogN
        本题可以O（N）的时间复杂度，O（1）的空间复杂度来求解 
        
        '''
        #使用hash的方式来求解
        #把每个位置出现的次数统计，找出出现2次的和0次的数字

        hashs=[0]*len(nums)
        missing=-1
        for i in range(len(nums)):
            hashs[nums[i]-1]+=1
        return [hashs.index(2)+1,hashs.index(0)+1]
