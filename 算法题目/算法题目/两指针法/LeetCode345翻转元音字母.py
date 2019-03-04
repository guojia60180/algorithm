#Author guo
class Solution:
    def reverseVowels(self, s):
        dic = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s[i].lower() in dic and s[j].lower() in dic:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i = i + 1
                j = j - 1

            elif s[i].lower() in dic and s[j].lower() not in dic:
                j = j - 1
            elif s[j].lower() in dic and s[i].lower() not in dic:
                i = i + 1
            else:
                i = i + 1
                j = j - 1

        return ''.join(s)

