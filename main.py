import sys

from Parser import *
def main():
    sys.set_int_max_str_digits(10000000)
    while True:

        expression = input("Enter expression: ")
        queue = expression_to_rpn(expression)
        l = []
        while not queue.is_empty():
            if isinstance(queue.head(),TokenType):
                l.append(queue.dequeue().value)
            else:
                l.append(queue.dequeue())
        print(l)
        res = evaluate(expression)
        if res is not None:
            print(expression, " = ", res)
        else:
            print("Invalid expression")
main()