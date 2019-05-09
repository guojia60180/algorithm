#Author guo
# -*- coding:utf-8 -*-
'''
数据平均分配到最大和最小堆中，两个堆中的数据数目差不能超过1
偶数分到最小堆，奇数分到最大堆
最大堆的所有数据都要小于最小堆中的数据

'''
import heapq
class Solution:
    def __init__(self):
        self.nums=[]
    def Insert(self, num):
        self.nums.append(num)
        # write code here
    def GetMedian(self):
        # write code here
        self.nums.sort()
        if len(self.nums)%2==1:
            return self.nums[(len(self.nums)-1)//2]
        else:
            return (self.nums[(len(self.nums)-1)//2]+self.nums[len(self.nums)//2])/2.0
class Solution1:
    def __init__(self):
        self.left = []
        self.right = []
    def Insert(self, num):
        from heapq import heappush, heappop
        #left 大堆 right 小堆
        if len(self.right) == 0 or num > self.right[0]:
            heappush(self.right, num)
        else:
            # push num的相反数进去，虽然left还是最小堆，但是里面的值都是相反数，反过来就是最大堆
            heappush(self.left, -num)
        # 不断调整两个堆，保证左右两个堆里元素的数量平衡
        while len(self.left) - len(self.right) > 1:
            data = -heappop(self.left)
            heappush(self.right, data)
        while len(self.right) - len(self.left) > 1:
            data = heappop(self.right)
            heappush(self.left, -data)

    def GetMedian(self,xxx):
        if len(self.left) == len(self.right):
            if len(self.right) == 0:
                return 0
            min_heap = self.right[0]
            max_heap = -1*self.left[0]
            media = (min_heap+max_heap)/2.0
            return media
        elif len(self.left) > len(self.right):
            media = -1*self.left[0]
            return media
        else:
            return self.right[0]