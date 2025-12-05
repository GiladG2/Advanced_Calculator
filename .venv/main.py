from Parser import *
from Stack import *
def main():
    while True:
        expression = input("Enter an expression: ")
        print(Evaluate(expression))

main()