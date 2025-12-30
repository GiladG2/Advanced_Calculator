def fac(n: int):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac


def max(n1: float, n2: float):
    if n1 > n2:
        return n1
    return n2


def min(n1: float, n2: float):
    if n1 < n2:
        return n1
    return n2


def average(n1: float, n2: float):
    return int(n1 + n2) / 2

def __is_numeric__(num:str):
    try:
        float(num)
        return True
    except ValueError:
        return False
print(__is_numeric__("-2"))

def hashtag_func(num:float):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num //10
    return sum