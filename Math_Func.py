def fac(n: float):
    if n == 1:
        return 1
    return n * fac(n - 1)


def max(n1: int, n2: int):
    if n1 > n2:
        return n1
    return n2


def min(n1: int, n2: int):
    if n1 < n2:
        return n1
    return n2


def average(n1: int, n2: int):
    return int(n1 + n2) / 2

def __is_numeric__(num:str):
    try:
        float(num)
        return True
    except ValueError:
        return False
print(__is_numeric__("-2"))
