#Author guo
import collections
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        C = collections.Counter(data)

        return C[k]

    def GetNumberofK2(self,data,k):
        number=0
        length=len(data)
        if data!=None and length>0:
            first=self.getfirstK(data,length,k,0,length-1)
            last=self.getlastK(data,length,k,0,length-1)

            if first>-1 and last>-1:
                number=last-first+1

        return number

    def getfirstK(self,data,length,k,start,end):
        if start>end:
            return -1

        middle=(start+end)//2
        middledata=data[middle]
        if middledata==k:
            if (middle>0 and data[middle-1]!=k) or middle==0:
                return middle
            else:
                end=middle-1

        elif middledata>k:
            end=middle-1
        else:
            start=middle+1

        return self.getfirstK(data,length,k,start,end)

    def getlastK(self,data,length,k,start,end):
        if start>end:
            return -1

        middle=(start+end)//2
        middledata=data[middle]

        if middledata==k:
            if (middle<length-1 and data[middle+1]!=k) or middle==length-1:
                return middle
            else:
                start=middle+1

        elif middledata<k:
            start=middle+1

        else:
            end=middle-1

        return self.getlastK(data,length,k,start,end)

