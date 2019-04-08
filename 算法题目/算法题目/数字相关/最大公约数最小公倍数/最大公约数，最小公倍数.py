#Author guo
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
#得到最大公约数

def lcm(a,b):
    return a*b/gcd(a,b)
#最小公倍数为两数乘积除以最大公约数

