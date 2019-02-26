#Author guo
class Solution:
    def maxArea(self, height):
        area = 0
        area_list = []
        left = right = 0
        right = len(height) - 1
        while left < right:
            l = height[left]
            r = height[right]
            if l < r:
                area = l * (right - left)
                area_list.append(area)

                left = left + 1
            else:
                area = r * (right - left)
                area_list.append(area)
                right = right - 1
        area_list.sort()
        return (area_list[-1])

#水的大小是最短边乘以两个的差