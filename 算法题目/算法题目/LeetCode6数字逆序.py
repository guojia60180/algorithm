#Author guo
class Solution:
    def reverse(self, x: int) -> int:

        Flag = 1
        if x < 0:
            Flag = -1
            strx = str(x)[1:]
        else:
            strx = str(x)

        x = int(strx[::-1])

        return 0 if x > pow(2, 31) else x * Flag