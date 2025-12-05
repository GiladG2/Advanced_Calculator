from Parser import *
from Stack import *
from Queue import *
from Tokens import *
def main():

    while True:
        expression = input("Enter expression: ")
        queue = expression_to_rpn(expression)
        l = []
        while not queue.is_empty():
            l.append(queue.dequeue())
        print(l)
        print(evaluate(expression))

main()