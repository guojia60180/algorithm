#Author guo
#Author guo
class Solution:
    def Fibonacci(self, n):
        # write code here
        a,b,counter=0,1,0
        while counter<n:
            a,b=b,b+a

            counter+=1

        return a

    def Fibonacci1(self,n):
        a,b,counter=0,1,0
        while counter<n:
            a,b=b,b+a
            yield a
            counter+=1





class Solution2:
    def Fibonacci(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]

    # 青蛙跳台阶, 每次可以跳1级或2级
    def jumpFloor(self, number):
        # write code here
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number + 1):
                tempArray[(i + 1) % 2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1) % 2]

    def jumpFloorII(self, number):
        ans = 1
        if number >= 2:
            for i in range(number-1):
                ans = ans * 2
        return ans

res=Solution()
print(res.Fibonacci1(20))
l=[]
for x in res.Fibonacci1(20):
    l.append(x)
    print(x)

print(l,end='.\n')
