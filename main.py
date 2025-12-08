from Parser import *
from Lexer import *

def main():
    while True:
        expression = input("Enter expression: ")
        queue = expression_to_rpn(expression)
        l = []
        while not queue.is_empty():
            l.append(queue.dequeue())
        print(l)
        print(expression,"=",evaluate(expression))
main()