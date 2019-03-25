#Author guo
'''
有一个容量N的背包，物品有两个属性，体积w和价值v

定义二维数组存储最大值，其中dp[i][j]表示前i件物品体积不超过j的情况下能达到的最大值
设第i件物品体积w，价值v，根据第i件物品是否添加背包中
分情况讨论

1.第i件物品没添加到背包，总体积不超过j的前i件物品的最大价值就是总体积不超过j的前i-1件物品的最大价值
dp[i][j]=dp[i-1][j]
2.第i件物品添加到背包里
dp[i][j]=dp[i-1][j-w]+v

'''
def bag(space,n,costs,values):
    """
    递归动态规划求解0/1规划
    :param :space 背包的总容量,int
    :param :n 表示拿前n件物品,int
    :param :costs 每个物品消耗的空间，list
    :param :values 每个物品的价值，list
    """
    if n == 0:  # 没东西拿了，递归结束，返回0
        return 0
    if space >= costs[n-1]:  # 放得下，那就比较拿和不拿两种情况
        return  max(bag(space,n-1,costs,values),bag(space-costs[n-1],n-1,costs,values) + values[n-1])
    else:  # 放不下，那就直接不拿
        return bag(space-costs[n-1],n-1,costs,values)

def bag(space,n,costs,values):
    """
    递归动态规划求解0/1规划
    :param :space 背包的总容量,int
    :param :n 表示物品的总数
    :param :costs 每个物品消耗的空间，list
    :param :values 每个物品的价值，list
    """
    costs.insert(0,0)  # 下标为0的值不使用
    values.insert(0,0) # 下标为0的值不使用
    # 构建一个行数为背包容量，列数为可用物品的矩阵 PS. 行或列下标为0的值均不用
    matrix = [[0 for _ in range(n+1)] for _ in range(space+1)]
    for i in range(1,space+1):  # 从小背包推到大背包
        for j in range(1,n+1):  # 遍历所有的物品
            if i >= costs[j]:  # 考虑拿这个物品的情况和不拿这个物品的情况哪个更好
                matrix[i][j] = max(matrix[i][j-1], matrix[i - costs[j]][j-1] + values[j])
            else: # 如果装不下, 那就相当于没有这个物品
                matrix[i][j] = matrix[i][j-1]
    return matrix[-1][-1]  # 返回最终值