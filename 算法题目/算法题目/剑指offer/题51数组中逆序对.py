#Author guo
#求逆序对
#1.拆分成两个子数组
#2.直到拆成两个长度为1的子数组
#3.长度为1的子数组合并排序，并统计逆序对
#4.长度为2的子数组合并排序，统计逆序对

# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        sortdata=sorted(data)
        res=0
        for x in sorted(data):
            #t=sortdata[0]
            res+=data.index(x)
            data.pop(data.index(x))

        return res
    #计算复杂度高，只能通过50%的数据

    def InversePairs1(self, data):
        return self.sort(data,0,len(data)-1,data)

    def sort(self,temp,left,right,data):
        if right-left<1:
            return 0
        if right-left==1:
            if data[left]<data[right]:
                return 0
            else:
                temp[left]=data[right]
                temp[right]=data[left]
                return 1
        mid=(left+right)//2
        res=self.sort(data,left,mid,temp)+self.sort(data,mid+1,right,temp)

        i=left
        j=mid+1
        index=left

        while i<=mid and j<=right:
            if data[i]<=data[j]:
                temp[index]=data[i]
                i+=1

            else:
                temp[index]=data[j]
                res+=mid-i+1
                j+=1