#Author guo
class Solution:
    def findLongestWord(self, s, d) :

        def is_subsequence(s,t):
            i=j=0
            m,n=len(s),len(t)

            if n>m:
                return False

            while i <m and j<n:
                if s[i]==t[j]:
                    i=i+1
                    j=j+1
                else:
                    i=i+1

            return j==n

        subseqence_length=0
        subseqence=''
        for string in d:
            if is_subsequence(s,string):
                if subseqence_length<len(string):
                    subseqence=string
                    subseqence_length=len(string)
                elif subseqence_length==len(string):
                    subseqence=min(subseqence,string)

        return subseqence


