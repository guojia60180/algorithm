#Author guo
# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s_list=s.split(' ')
        #print(s_list)
        rev_s=reversed(s_list)
        return ' '.join(rev_s)

s=Solution()
s.ReverseSentence("I am a student.")