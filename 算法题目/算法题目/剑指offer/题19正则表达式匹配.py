#Author guo
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not s  or not pattern :
            return False
        if s==pattern:
            return True

        elif pattern=='':
            return False
        #利用字符串的切片来进行
        #当s为'',如果pattern为'.'返回True
        #如果pattern长度为1且不为;'.',或者不为*，pattern不可能为空，返回False
        #pattern长度不为1，且第二个字符*，pattern还有空的可能，从第三个开始迭代
        elif s=='':
            if pattern=='.':
                return True
            elif len(pattern)==1 or pattern[1]!='*':
                return False
            else:
                return self.match(s,pattern[2:])

        #如果pattern长度不小于2，且pattern的第二个字符不是*的情况下
        #当pattern[0]不等于s[0]且不为.的时候，s和pattern必不相等
        #否则，s和pattern右移一位继续比较
        if len(pattern)>=2 and pattern[1]!='*':
            if s[0]!=pattern[0] and pattern[0]!='.':
                return False
            else:
                return self.match(s[1:],pattern[1:])

        #如果pattern惨淡股不小于2，且第二个字符为*的情况
        #如果s[0]不等于pattern[0]，且pattern[0]不为'.'
        #第一位比较不成功，pattern必须后移两位比较
        #如果s[0]等于pattern[0] 或者pattern[0]为.第一位匹配
            #1.aaa和a*a情况，星号代表多个a，s不断右移一位比较
            #2.a和a*a情况，星号代表0个a,s不需要右移 pattern右移两位
            #3.abc和a*bc情况，星号代表1个a，s右移一位，pattern右移两位继续比较

        elif len(pattern)>=2 and pattern[1]=='*':
            if s[0]!=pattern[0] and pattern[0]!='.':
                return self.match(s,pattern[2:])

            else:
                return self.match(s[1:],pattern) or self.match(s,pattern[2:]) or self.match(s[1:],pattern[2:])

        elif pattern=='.' and len(s)==1:
            return True
        return False

s = Solution()
print(s.match('', '.'))