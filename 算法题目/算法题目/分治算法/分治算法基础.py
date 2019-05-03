#Author guo
#一般都伴随递归

#分治算法实现查找数组中最大元素位置
def maxIndex(list,start,end):
    if start>end or len(list)==0:
        return

    pivot=(start+end)//2

    if end-start==1:
        return start
    else:
        temp1=maxIndex(list,start,pivot)
        temp2=maxIndex(list,pivot,end)

        if list[temp1]<list[temp2]:
            return temp2
        else:
            return temp1

print(maxIndex([5,7,9,3,4,8,6,2,0,1], 0, 9))

#分治计算正整数幂
def power(base,x):
    if x==1:
        return base
    else:
        if x&1==1:
            return power(base,x//2)*power(base,x//2)*base
        else:
            return power(base,x//2)*power(base,x//2)

print(power(2,6))