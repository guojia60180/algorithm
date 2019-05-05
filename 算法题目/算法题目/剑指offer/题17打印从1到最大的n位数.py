#Author guo
'''
输入数字n, 按顺序打印从1最大的n位十进制数
比如输入3, 则打印出1、2、3、到最大的3位数即999
'''

def Print1toMaxOfDigits(n):
    if n<=0:
        return

    numbers=['0']*n
    for i in range(10):
        numbers[0]=str(i)
        Print1ToMaxOfDigitsRec(numbers,n,0)
def PrintNumber(number):
    isBeginning0 = True
    nLength = len(number)

    for i in range(nLength):
        if isBeginning0 and number[i] != '0':
            isBeginning0 = False
        if not isBeginning0:#如果开头没
            print('%c' % number[i], end='')
    print('')
def Print1ToMaxOfDigitsRec(number,length,index):
    if index==length-1:
        PrintNumber(number)

        return

    for i in range(10):
        number[index+1]=str(i)
        Print1ToMaxOfDigitsRec(number,length,index+1)
Print1toMaxOfDigits(2)