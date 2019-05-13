#Author guo
#n个骰子上面的总和为s，输入n，打印s的所有值出现的概率
#n-6n之间的所有值都有可能出现

# -*- coding:UTF-8 -*-
'''
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的概率
我们将n个骰子分成两堆，一堆为1个骰子，另一堆为n-1个骰子，单独的那一个出现的点数为1~6。我们需要计算n-1个骰子来计算点数和，我们对n-1个骰子再次进行同样的划分。我们用f(n)表示n个骰子出现的点数，f(n)=f(n-1)+f(n-2)+f(n-3)+f(n-4)+f(n-5)+f(n-6)。很显然我们可以用递归实现。
--------------------- 

'''

def PrintProbability(number):
    if number<=0:
        return
    pros=[0]*(6*number-number+1)#共有的总和点数可能
    Probaility(pros,number)
    total=pow(6,number)

    for i in range(number,6*number+1):
        print(i+':'+pros[i-number]+'/'+total)

def Probaility(pros,number):
    for i in range(1,7):
        helper(number,number,i,pros)

def helper(original,current,sum,pros):
    if current==1:
        pros[sum-original]+=1

    else:
        for i in range(1,7):
            helper(original,current-1,i+sum,pros)

# 基于循环求点数, 时间性能好
def PrintProbability(number):
    if number < 1:
        return
    maxVal = 6
    # 构造两个数组来存储骰子点数的每一个总数出现的次数
    # 在一次循环中, 第一个数组中的第n个数字表示骰子和为n出现的次数
    # 在下次循环中, 另一个数组的第n个数字设为前一个数组对应的第n-1、n-2、n-3、n-4、n-5、n-6之和
    probStorage = [[], []]
    probStorage[0] = [0]*(maxVal * number + 1)
    flag = 0
    for i in range(1, maxVal+1):
        probStorage[flag][i] = 1
    for time in range(2, number+1):
        probStorage[1-flag] = [0]*(maxVal * number + 1)
        for pCur in range(time, maxVal*time+1):
            diceNum = 1
            while diceNum < pCur and diceNum <= maxVal:#值小于6
                probStorage[1-flag][pCur] += probStorage[flag][pCur-diceNum]#5个相加
                diceNum += 1
        flag = 1 - flag
    total = maxVal ** number
    for i in range(number, maxVal*number+1):
        ratio = probStorage[flag][i] / float(total)
        print("{}: {}".format(i, ratio))
s = PrintProbability(5)
print(s)
