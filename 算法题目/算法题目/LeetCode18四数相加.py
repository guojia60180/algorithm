#Author guo
class Solution(object):
 def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result=[]
    length=len(nums)
    nums.sort()
    for i in range(0,length-3):
        if i!=0 and nums[i]==nums[i-1]:
            continue
        if nums[i]*4>target:
            break
        for j in range(length-1,i+2,-1):
            if j!=length-1 and nums[j]==nums[j+1]:
                continue
            if nums[j]*4<target:
                break
            sub2=target-nums[i]-nums[j]
            low,high=i+1,j-1
            while low<high:
                sum2=nums[low]+nums[high]
                if sum2>sub2:
                    high-=1
                elif sum2<sub2:
                    low+=1
                else:
                    ans = [nums[i],nums[low],nums[high],nums[j]]
                    ans.sort()
                    result.append(ans)
                    while low<high and nums[low+1]==nums[low]:
                        low+=1
                    while low<high and nums[high-1]==nums[high]:
                        high-=1
                    high,low=high-1,low+1
    return result

 #先取了边界，然后判断完后，两个两个分别将进行判断，循环