#Author guo
def digitAtIndex(index):
    if index < 0:
        return -1
    digits = 1
    while True:
        numbers = countOfIntegers(digits)
        if index < numbers * digits:
            return digitAtIndexWithMDigits(index, digits)
        index -= numbers * digits
        digits += 1


def countOfIntegers(digits):
    """输入1，返回0-9的个数10；输入2，返回10-99的个数90；输入3，返回100-999的个数900"""
    if digits == 1:
        return 10
    count = 9 * pow(10, digits - 1)
    return count


def digitAtIndexWithMDigits(index, digits):
    """在直到index指向的数是m位数的前提下，返回index指向的数字"""
    # 找到index指向的这个数是属于哪个整数
    number = beginNumber(digits) + index // digits
    indexFromRight = digits - index % digits
    for i in range(1, indexFromRight):
        number = number // 10
    return number % 10


def beginNumber(digits):
    """返回m位数的第一个数"""
    if digits == 1:
        return 0
    return pow(10, digits - 1)