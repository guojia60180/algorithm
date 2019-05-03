#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length=len(rotateArray)
        l=0
        r=length-1
        find=0
        while rotateArray[l]>=rotateArray[r]:
            if r-l==1:
              find=r
              break
            find=(l+r)//2
            if rotateArray[find]>=rotateArray[l]:
                l=find
            elif rotateArray[find]<=rotateArray[r]:
                r=find

        return rotateArray[find]
