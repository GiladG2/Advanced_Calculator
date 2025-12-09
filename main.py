from Parser import *

def main():
    while True:
        expression = input("Enter expression: ")
        res = evaluate(expression)
        if res is not None:
            print(expression, " = ", res)
        else:
            print("Invalid expression")
main()