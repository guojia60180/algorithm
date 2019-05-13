#Author guo

def MaxDiff(numbers):
    if numbers==None and len(numbers)<2:
        return 0

    Min=numbers[0]
    Max=numbers[1]-Min

    for i in range(2,len(numbers)-1):
        if numbers[i-1]<Min:
            Min=numbers[i-1]

        curDiff=numbers[i]-Min
        if curDiff>Max:
            Max=curDiff

    return Max