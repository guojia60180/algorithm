    #Author guo
import collections
class Solution:
    def singleNumber(self, nums):
            #两个相同的数异或结果为0，对所有数进行异或操作
            #最后结果就是单独出现的数
        ret=0
        for n in nums:
            ret=ret^n

        return ret


    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key
        #建立counter表

    def singleNumber2(self, nums):
        d=collections.Counter(nums)

        for key,val in d.items():
            if val==1:
                return key