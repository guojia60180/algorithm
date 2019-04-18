#Author guo
class Solution:
    def singleNumber(self, nums):
        #两个不相等的元素必定至少有一位不同
        #将数组元素异或得到结果是不存在重复的两个元素异或的结果
        #diff&=-diff 得到diff右侧不为0的位
        diff=0
        for num in nums:
            diff^=num
        diff&=-diff#得到最右边一位
        ret=[0]*2
        for num in nums:
            if num&diff==0:
                ret[0]^=num
            else:
                ret[1]^=num

        return ret