#Author guo
import collections
class Solution:
    def maxProduct(self, words):
        #int 有32位 对于一个字符串，把出现字符对应到int上
        #就可以作为字符串的识别码
        #只要两个字符串摘要与一下，结果0
        #两个字符串没有公共子串
        res=0
        d=collections.defaultdict(int)
        N=len(words)
        for i in range(N):
            w=words[i]
            for c in w:
                d[w]|=1<<(ord(c)-ord('a'))
            for j in range(i):
                if not d[words[j]]&d[words[i]]:#判断是否相同
                    res=max(res,len(words[j])*len(words[i]))
        return res

    def maxProduct2(self, words):
            """
            :type words: List[str]
            :rtype: int
            """
            word_dict = dict()
            for word in words:
                word_dict[word] = set(word)
            max_len = 0
            for i1, w1 in enumerate(words):
                for i2 in range(i1 + 1, len(words)):
                    w2 = words[i2]
                    if not (word_dict[w1] & word_dict[w2]):
                        max_len = max(max_len, len(w1) * len(w2))
            return max_len

