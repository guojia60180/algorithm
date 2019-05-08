#Author guo
# -*- coding:utf-8 -*-
import collections

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        #最简单思路是排序，输出前几个就好
        if tinput==None or len(tinput)<k or len(tinput)<=0 or k<=0:
            return []
        n=len(tinput)
        start=0
        end=n-1
        index=self.Partition(tinput,n,start,end)
        while index!=k-1:
            if index>k-1:
                end=index-1
                index=self.Partition(tinput,n,start,end)
            else:
                start=index+1
                index=self.Partition(tinput,n,start,end)

        out=tinput[:k]
        out.sort()
        return out

    def Partition(self,numbers,length,start,end):
        if numbers==None or length<=0 or start<0 or end>=length:
            return None
        if end==start:
            return end
        pivot=numbers[start]
        left=start+1
        right=end

        done=False

        while not done:
            while numbers[left]<=pivot and left<=right:
                left+=1

            while numbers[right]>=pivot and right>=left:
                right+=1

            if left>right:
                done=True

            else:
                numbers[left],numbers[right]=numbers[right],numbers[left]
        numbers[right],numbers[start]=numbers[start],numbers[right]
        return right

    def GetLeastNumbers_Solution2(self, tinput, k):
        import heapq
        #海量数据处理的方式，主要堆的方式进行
        if tinput==None or len(tinput)<k or len(tinput)<=0 or k<=0:
            return []
        out=[]
        for num in tinput:
            if len(out)<k:
                out.append(num)

            else:
                out=heapq.nlargest(k,out)
                if num>=out[0]:
                    continue#如果大于最大值，跳出本次循环
                else:
                    out[0]=num#小于最大值，把根结点设置为这个数，最大堆自动调整

        return sorted(out[::-1])
