#Author guo
#二分图如果可以用两种颜色对图中节点进行着色，保证相邻节点颜色不同
#那么这个图就是二分图
import collections
class Solution:
    def isBipartite(self, graph):
        visited=[0]*len(graph)
        for i in range(len(graph)):
            if graph[i] and visited[i]==0:
                visited[i]=1

                q=collections.deque()
                q.append(i)
                while q:
                    v=q.popleft()
                    for e in graph[v]:
                        if visited[e]!=0:
                            if visited[e]==visited[v]:
                                return False
                        else:
                            visited[e]=3-visited[v]
                            q.append(e)
        return True
'''
众所周知的染色法。可以通过BFS或者DFS来解决。我使用的是BFS.

使用一个visited数组来保存每个节点被染的颜色。
0代表没染色，1代表染成蓝色，2代表染成红色。
对图的每个顶点进行一个遍历，把和这个顶点相邻的顶点全部染成相反的颜色。
如果相邻顶点已经染色，而且染色和当前顶点染色相同，则返回False。
全部成功染色后返回True。

这个题没有说明是连通图，这个就很坑爹了，
不能通过一次的BFS就把所有的顶点染色成功
所以需要的是一个外层的对顶点进行遍历，
一个内层的对每个顶点相邻的顶点遍历，
这样两重遍历才能保证每个顶点、这个顶点相邻的顶点都被强行的染色。

时间复杂度是O(E+V)，空间复杂度是O(E).
'''