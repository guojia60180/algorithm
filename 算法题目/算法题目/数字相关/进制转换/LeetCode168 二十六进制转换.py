#Author guo
class Solution:
    def convertToTitle(self, n):
        if n==0:
            return ''
        n=n-1

        return self.convertToTitle(n/26)+chr(n%26+65)
