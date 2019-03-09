#Author guo
class Solution:
    def mySqrt(self, x):
        # if x==1:
        #     return 1
        # if not x:
        #     return 0
        l = 0
        r = x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid

            elif mid * mid > x:
                r = mid - 1

            else:
                l = mid + 1

