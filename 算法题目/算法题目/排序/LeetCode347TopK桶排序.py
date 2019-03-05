#Author guo
#设置若干个桶，每个桶存储出现频率相同的数
#桶的下标代表桶中数出现的频率
#i个桶中存储的数出现的频率是i
class Solution:
    class Solution:
        def topKFrequent(self, nums, k):
            """
            :type nums: List[int]
            :type k: int
            :rtype: List[int]
            """
            dict1 = {}
            result = []
            for i in range(len(nums)):
                if nums[i] in dict1:
                    dict1[nums[i]] += 1
                else:
                    dict1[nums[i]] = 1
            for i in range(k):
                m = max(dict1, key=dict1.get)
                result.append(m)
                del dict1[m]
            return result

