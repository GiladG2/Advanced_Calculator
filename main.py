import sys

from Parser import *
from Math_Func import fac
def main():
    sys.set_int_max_str_digits(10000000)
    res = fac(10000)
    while True:
        expression = input("Enter expression: ")
        res = evaluate(expression)
        if res is not None:
            print(expression, " = ", res)
        else:
            print("Invalid expression")
main()