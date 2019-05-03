#Author guo
#解决动态规划的找零问题
#输入需要找零的金额和货币的币值向量
#输出满足找零条件下的最少硬币个数

def ChangeMaking(coinVal,change):
    list=[0]*(change+1)
    for i in range(1,change+1):
        temp=change
        j=0
        while j<=len(coinVal)-1 and i>=coinVal[j]:
            temp=min(list[i-coinVal[j]],temp)
            j+=1
        list[i]=temp+1

    return list.pop()
print(ChangeMaking([1,5,10,25],63))

#解决动态规划币值最大问题
#为满足所选硬币不相邻的条件下，从一堆硬币中选择最大金额的硬币
#输入数组C[1...n]保存n个硬币面值
#输出可选硬币的最大金额

def coinRow(coinrow):
    list=[0]*(len(coinrow)+1)
    list[1]=coinrow[0]
    for i in range(2,len(coinrow)+1):
        list[i]=max(coinrow[i-1]+list[i-2],list[i-1])

    return list.pop()

print(coinRow([5,1,2,10,6,2]))


#解决0-1背包问题
def maxBag(weight,value,totalweight):
    if len(weight)<=0 or len(value)<=0 or totalweight<=0 or len(weight)!=len(value):
        return
    num=len(weight)

    tempmat=[]
    for i in range(num+1):
        tempmat.append([0]*(totalweight+1))
    for i in range(1,num+1):
        for j in range(1,totalweight+1):
            if j-weight[i-1]>=0:
                tempmat[i][j]=max(tempmat[i-1][j],value[i-1]+ tempmat[i-1][j-weight[i-1]])
            else:
                tempmat[i][j]=tempmat[i-1][j]
    return tempmat[-1][-1]

weight, value, totalWeight = [2,1,3,2], [12,10,20,15], 5
print(maxBag(weight, value, totalWeight))