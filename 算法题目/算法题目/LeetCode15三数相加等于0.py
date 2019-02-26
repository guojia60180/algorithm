class Solution:
    def threeSum(self, nums):
        l = 0

        res = []
        tmp = []
        nums.sort()
        for l in range((len(nums) - 2)):
            i = l + 1
            r = len(nums) - 1

            while l < i and i < r:
                summ = nums[l] + nums[i] + nums[r]
                if summ == 0:
                    tmp = [nums[l], nums[i], nums[r]]
                    res.append(tmp)
                    i = i + 1
                elif summ > 0:
                    r = r - 1
                else:
                    i = i + 1
        res = set(map(tuple, res))
        return list(res)

