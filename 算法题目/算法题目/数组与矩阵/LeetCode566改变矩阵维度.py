#Author guo
class Solution:
    def matrixReshape(self, nums, r,c):
        m=len(nums)
        n=len(nums[0])
        if m*n!=r*c:
            return nums
        res=[]
        row=[]
        for i in range(m):
            for j in range(n):
                row.append(nums[i][j])
                if len(row)==c:
                    res.append(row)
                    row=[]

        return res