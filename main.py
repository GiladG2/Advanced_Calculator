from Parser import *
from Stack import *
from Queue import *
def main():
    while True:
        expression = input("Enter expression: ")
        print(evaluate(expression))
main()