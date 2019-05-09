#Author guo
#动态规划
#f(i,j)=max(f(i-1,j),f(i,j-1))+gift[i,j]

def getMaxValue(values):
    rows=len(values)
    cols=len(values[0])

    if values==None or rows<=0 or cols<=0:
        return 0
    maxValues=[0]*cols
    for i in range(rows):
        for j in range(cols):
            left=up=0
            if i>0:
                up=maxValues[j]
            if j>0:
                left=maxValues[j-1]

            maxValues[j]=max(left,up)+values[i][j]
    maxValue=maxValues[cols-1]

    return maxValue