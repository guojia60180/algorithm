#Author guo
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        res = nums[0] + nums[1] + nums[2]
        l = 0

        for l in range((len(nums) - 2)):
            i = l + 1
            r = len(nums) - 1

            while l < i and r > i:
                summ = nums[l] + nums[i] + nums[r]
                if summ == target:
                    return target
                elif abs(summ - target) < abs(res - target):
                    res = summ#判断如果和与目标差绝对值小于res与目标值差，替换res
                elif summ > target:

                    r = r - 1
                else:

                    i = i + 1
        return res
