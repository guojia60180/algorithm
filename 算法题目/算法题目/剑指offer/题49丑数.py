# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        if index == 1:
            return 1
        ans = [1]
        a, b, c = 0, 0, 0

        for i in range(1, index):
            ans.append(min(ans[a] * 2, ans[b] * 3, ans[c] * 5))
            if ans[i] == ans[a] * 2:
                a += 1
            if ans[i] == ans[b] * 3:
                b += 1
            if ans[i] == ans[c] * 5:
                c += 1

        return ans[index - 1]
