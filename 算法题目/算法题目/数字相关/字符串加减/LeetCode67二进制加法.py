#Author guo
class Solution:
    def addBinary(self, a, b):
        M, N = len(a), len(b)
        if M < N:
            a = "0" * (N - M) + a
        else:
            b = "0" * (M - N) + b
        stack1 = list(a)
        stack2 = list(b)
        res = ""
        carry = 0
        while stack1 and stack2:
            s1, s2 = stack1.pop(), stack2.pop()
            cursum = int(s1) + int(s2) + carry
            if cursum >= 2:
                cursum %= 2
                carry = 1
            else:
                carry = 0
            res = str(cursum) + res
        if carry:
            res = "1" + res
        return res


