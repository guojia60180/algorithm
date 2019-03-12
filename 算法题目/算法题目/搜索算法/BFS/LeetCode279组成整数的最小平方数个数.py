#Author guo
#每个整数看成图中的一个点，如果两个整数之间相差一个平方数
#这两个节点之间就有一条边

#从节点n到节点0的最短路径

class Solution:
    def numSquares(self,n):
        q=list()
        q.append([n,0])
        visited=[False for _  in range(n+1)]
        visited[n]=True
        #创建队列，并且对队列中的n值置位True

        #遍历队列里节点
        while any(q):
            num,step=q.pop(0)

            i=1
            tnum=num-i**2
            while tnum>0:
                if tnum==0:
                    return step+1
                #先到达0的一定步数最小
                if not visited[tnum]:
                    q.append((tnum,step+1))
                    visited[tnum]=True

                i=i+1
                tnum=num-i**2

