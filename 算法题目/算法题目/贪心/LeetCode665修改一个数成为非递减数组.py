#Author guo
#判断一个数组能不能只修改一个数就能成为非递减数列

class Solution:
    def checkPossibility(self, nums):
        count=0
        if len(nums)<=2:
            return True

        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>=0:
                pass
            else:
                count+=1
                if i==1 or nums[i-2]<=nums[i]:
                    nums[i-1]=nums[i]#变成小的
                else:
                    nums[i]=nums[i-1]#变成大的

                if count>1:
                    return False

        return True
'''
class Solution1(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True
        a1=nums[:]
        a2=nums[:]
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                a1[i]=nums[i+1]
                a2[i+1]=nums[i]
                break
        return a1==sorted(a1) or a2==sorted(a2)
对nums数组复制两份a1，a2。其中一份改大，另一份改小，且只改动一次就直接break，结束遍历。然后a1和对a1进行排序后进行比较，a2和对a2进行排序后进行比较，只要其中一个是相等的，就可返回true，否则返回false。这种Python写起来比较方便。
'''
