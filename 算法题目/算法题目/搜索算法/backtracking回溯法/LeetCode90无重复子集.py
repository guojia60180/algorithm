#Author guo
class Solution:
    def subsetsWithDup(self, nums):
        if nums == None:
            return []
        res = []
        self.dfs(0, sorted(nums), res, [])
        res2 = []
        for x in res:
            if x not in res2:
                res2.append(x)#判断重复，需要额外申请一块空间

        return res2

    def dfs(self, i, nums, res, subsetres):
        res.append(subsetres)
        for j in range(i, len(nums)):
            self.dfs(j + 1, nums, res, subsetres + [nums[j]])