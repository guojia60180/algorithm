#Author guo
class Solution:
    def combinationSum4(self, nums, target) :
        #完全背包

        mem=[0]*(target+1)
        mem[0]=1
        for i in range(1,target+1):
            for num in nums:
                if i>=num:
                    mem[i]=mem[i]+mem[i-num]

        return mem[target]
