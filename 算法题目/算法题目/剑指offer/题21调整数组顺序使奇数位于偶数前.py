#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):#没有满足顺序
        # write code here
        if not array:
            return

        l=0
        r=len(array)-1
        while l<r:
            while l<r and array[l]%2!=0:
                l+=1
            while l<r and array[r]%2!=1:
                r-=1

            if l<r:
                array[l],array[r]=array[r],array[l]

        return array

    def reOrderArray2(self, array):
        left=[x for x in array if x%2==1]
        right=[x for x in array if x%2==0]
        return left+right


    def reOrderArray3(self, array):
            if len(array) < 1:
                return []
            if len(array) == 1:
                return array
            arrayOdd = []
            arrayEven = []
            for num in array:
                if num & 0x1:
                    arrayOdd.append(num)
                else:
                    arrayEven.append(num)
            return arrayOdd + arrayEven