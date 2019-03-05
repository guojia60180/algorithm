#Author guo
#对于求解kth Element问题，使用快速排序
#需要打乱数组，否则会造成最坏情况
#对于求解TopK Element问题，最好先hash存储
#再对出现自出进行排序，使用堆排序来做，用最大堆按照映射次数从大到小排列

class Solution:
    def findKthLargest(self, nums, k):
        l,r=0,len(nums)-1
        nums=self.quick_sort(nums,l,r)
        #print(nums)
        return nums[-k]

    def quick_sort(self,nums,l,r):
        if l<r:
            pivot=self.partition(nums,l,r)

            self.quick_sort(nums,l,pivot-1)
            self.quick_sort(nums,pivot+1,r)
        return nums


    def partition(self,nums,l,r):
        pivot=nums[l]
        while l<r:
            while l<r and nums[r]>=pivot:
                r=r-1
            nums[l]=nums[r]
            while l<r and nums[l]<=pivot:
                l=l+1
            nums[r]=nums[l]#如果右边的小于pivot，交换位置
            #因为是从l=0取的因此不存在左边大于pivot的情况

        nums[l]=pivot#交换完成
        return l#移到了中间
s=Solution()
print(s.findKthLargest([2,4,5,1,3],2))
