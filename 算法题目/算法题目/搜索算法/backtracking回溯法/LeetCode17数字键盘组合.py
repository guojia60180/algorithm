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
            x = self.letterCombinations(digits[1:])
            for r in x:
                for j in a[digits[0]]:
                    res.append(j + r)#当成两个元素，循环遍历所有的结果
                    #digits传入key值，直接调用，a[key]=value值进行循环遍历
        return res