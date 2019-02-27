#Author guo
class Solution:
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
class Solution:
    def strStr(self, haystack, needle):
        if len(haystack)<len(needle):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            found=True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    found = False#迭代查找，效率比较低
                    break
            if found:
                return i
        return -1