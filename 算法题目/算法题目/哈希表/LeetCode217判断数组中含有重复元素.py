#Author guo
'''
思路1：把数组排序，只需要遍历一次，当前元素与下一个元素比较
思路2：集合的性质，集合去重，因此只需要比较原数组长度和集合长度
思路3：哈希字典 将出现过的数记录下来，遍历下一个数时看是否出现

'''
class Solution:
    def containsDuplicate(self, nums):
        map={}
        for i in nums:
            if i in map:
                return True
            map[i]=True

        return False
