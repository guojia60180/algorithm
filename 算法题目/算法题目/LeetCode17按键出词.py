#Author guo
class Solution:
    def letterCombinations(self, digits):
        a = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return list(a[digits[0]])

        else:
            x = self.letterCombinations(digits[1:])#递归实现
            for r in x:
                for j in a[digits[0]]:
                    res.append(j + r)
        return res