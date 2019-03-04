#Author guo

class Solution:
    def permute(self, nums):
        res=[]
        self.dfs(nums,res,[])
        return res


    def dfs(self,nums,res,path):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:],res,path+[nums[i]])

    #或者利用回溯法


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [0] * len(nums)
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0

        dfs([])
        return res



