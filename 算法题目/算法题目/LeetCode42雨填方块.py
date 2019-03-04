#Author guo
class Solution(object):
    def trap(self, height):
        n=len(height)
        if n<=1:
            return 0
        left=[0 for i in range(n)]
        right=[0 for i in range(n)]
        left[0],right[-1]=height[0],height[-1]

        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])

        total_water=0

        for i in range(n):
            temp=min(left[i],right[i])-height[i]
            total_water=temp+total_water

        return total_water

