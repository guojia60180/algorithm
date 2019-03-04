#Author guo
class Solution:
    def myPow(self, x, n):
        if n<0:
            x=1/x
            n=-n
        pow=1

        while n:
            if (n%2):
                pow=pow*x
            x=x*x
            n=n//2
        return pow

