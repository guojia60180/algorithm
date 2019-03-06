#Author guo
# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        #计算最多组成的不重叠区间个数，区间总数-不重叠的个数
        #按区间结尾进行排序，每次选择结尾最小，且和前一个区间不重叠的区间
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)#根据起始点把区间排序
        curr,cnt=intervals[0].end,0#初始化

        for x in intervals[1:]:
            if x.start<curr:
                cnt+=1
                curr=min(curr,x.end)#每次更新最小的end值
            else:
                curr=x.end

        return cnt

