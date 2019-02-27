#Author guo

class Solution:
 def divide(self, dividend, divisor):
    max_int = 2147483647
    min_int = -2147483648
    if dividend == min_int and divisor == -1:
        return max_int
    signal = 1
    if dividend < 0:
        signal = -signal
    if divisor < 0:
        signal = -signal
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        d, times = divisor, 1
        while d <= dividend:
            d <<= 1
            times <<= 1
        d >>= 1
        times >>= 1
        res += times
        dividend -= d
    return res * signal
 #利用位方法来做。替代除法