#Author guo
#递归求和

def listsum(numlist):
    if len(numlist)==1:
        return numlist[0]
    else:
        return numlist[0]+listsum(numlist[1:])

#递归阶乘

def listFactorial(num):
    if num<=1:
        return 1
    else:
        return num*listFactorial(num-1)

#递归实现进制转换

def tostr(n,base):
    convertString='0123456789ABCDEF'

    if n<base:
        return convertString[n]
    else:
        return tostr(n//base,base)+convertString[n%base]


# 递归实现Hanoi塔
def Hanoi(fromPole, withPole, toPole, diskNum):
    if diskNum <= 1:
        print("moving disk from %s to %s" % (fromPole, toPole))
    else:
        Hanoi(fromPole, toPole, withPole, diskNum-1)
        print("moving disk from %s to %s" % (fromPole, toPole))
        Hanoi(withPole, fromPole, toPole, diskNum-1)

Hanoi('A', 'B', 'C', 3)