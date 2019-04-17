#Author guo\
import heapq
class Solution:
    def kthSmallest1(self, matrix, k):
        m=len(matrix)
        n=len(matrix[0])
        lo=matrix[0][0]
        hi=matrix[m-1][n-1]

        while lo<=hi:
            cnt=0
            mid = (lo + hi) // 2
            j=n-1
            for i in range(m):
                while j>=0 and matrix[i][j]>mid:
                    j=j-1
                cnt+=j+1
            if cnt<k:
                lo=mid+1
            else:
                hi=mid-1

        return lo

    def kthSmallest2(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        lo = matrix[0][0]
        hi = matrix[m - 1][n - 1]

        while lo <= hi:
            mid = (lo + hi) // 2
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        cnt += 1
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

    def kthSmallest3(self, matrix, k):
            """
            :type matrix: List[List[int]]
            :type k: int
            :rtype: int
            """
            nums = []
            for line in matrix:
                nums.extend(line)
            heapq.heapify(nums)
            res = 0
            for i in range(k):
                res = heapq.heappop(nums)
            return res

    #堆方法改进
    #不需要把每个元素都进堆，只是把最可能小值的进堆
    #把最上角最小元素和索引进堆，堆中的元素遍历，每次把元素右边的元素进堆
    #当是第一列元素时，把这个元素下面的元素也进堆
    def kthSmallest4(self, matrix, k):
        m,n=len(matrix),len(matrix[0])
        q=[(matrix[0][0],0,0)]
        ans=0
        for _ in range(k):
            ans,i,j=heapq.heappop(q)
            if j==0 and i+1<m:
                heapq.heappush(q,(matrix[i+1][j],i+1,j))
            if j+1<n:
                heapq.heappush(q,(matrix[i][j+1],i,j+1))
        return ans