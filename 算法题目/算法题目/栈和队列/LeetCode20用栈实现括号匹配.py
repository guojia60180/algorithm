#Author guo
class Solution:
    def isValid(self, s):
        stack = []

        for p in s:
            if p in '{[(':
                stack.append(p)
            else:
                if not stack:
                    return False
                elif p == '}' and stack.pop() != '{':
                    return False
                elif p == ']' and stack.pop() != '[':
                    return False
                elif p == ')' and stack.pop() != '(':
                    return False
        return (stack == [])