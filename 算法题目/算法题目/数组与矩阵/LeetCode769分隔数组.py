#Author guo
#分隔数组。使得每部分排序后数组有序
class Solution:
    def maxChunksToSorted(self, arr):
        chunks=0
        pre_max=0
        for i,num in enumerate(arr):
            if num>pre_max:
                pre_max=num
            if pre_max==i:
                chunks+=1

        return chunks
