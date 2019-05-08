#Author guo
# -*- coding:utf-8 -*-
import collections
class Solution:
    def MoreThanHalfNum_Solution1(self, numbers):
        # write code here
        dic=collections.Counter(numbers).most_common()
        if dic[0][1]>(len(numbers)//2):
            return dic[0][0]
        else:
            return 0

    def MoreThanHalfNum_Solution(self, numbers):
        length=len(numbers)
        if numbers==None or length<=0:
            return 0
        res=numbers[0]
        times=0
        for i,num in enumerate(numbers):
            if times==0:
                res=num
                times=1
            elif res==num:
                times+=1
            else:
                times-=1

        return res if numbers.count(res)>length//2 else 0

    def MoreThanHalfNum_Solution3(self, numbers):
        length = len(numbers)
        if length == 1:
            return numbers[0]
        if self.CheckInvalidArray(numbers, length):
            return 0

        middle = length >> 1
        start = 0
        end = length - 1
        index = self.Partition(numbers, length, start, end)
        while index != middle:
            if index > middle:
                end = index - 1
                index = self.Partition(numbers, length, start, end)
            else:
                start = index + 1
                index = self.Partition(numbers, length, start, end)
        result = numbers[middle]
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result
    # 划分算法
    def Partition(self, numbers, length, start, end):
        if numbers == None or length <= 0 or start < 0 or end >= length:
            return None
        if end == start:
            return end
        pivotvlue = numbers[start]
        leftmark = start + 1
        rightmark = end

        done = False

        while not done:
            while numbers[leftmark] <= pivotvlue and leftmark <= rightmark:
                leftmark += 1
            while numbers[rightmark] >= pivotvlue and rightmark >= leftmark:
                rightmark -= 1

            if leftmark > rightmark:
                done = True
            else:
                numbers[leftmark], numbers[rightmark] = numbers[rightmark], numbers[leftmark]
        numbers[rightmark], numbers[start] = numbers[start], numbers[rightmark]
        return rightmark

    # 检查输入的数组是否合法
    def CheckInvalidArray(self, numbers, length):
        InputInvalid = False
        if numbers == None or length <= 0:
            InputInvalid = True
        return InputInvalid
    # 检查查找到中位数的元素出现次数是否超过所有元素数量的一半
    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        if times*2 <= length:
            return False
        return True