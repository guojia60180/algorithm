#Author guo
class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        points=sorted(points)
        cnt=1
        end=points[0][1]

        for x in points[1:]:
            if end>=x[0]:

                end=min(end,x[1])
                continue
            cnt += 1
            end=x[1]

        return cnt
