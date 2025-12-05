from Queue import Queue
from Stack import Stack
from TokenType import *


def evaluate(expression:str) -> float:
    return eval_rpn(expression_to_rpn(expression))
def expression_to_rpn(expression:str) -> Queue:
    stack = Stack()
    queue = Queue()
    i=0
    while i <len(expression):
        val = 0
        current : TokenType = None
        if not stack.is_empty():
            current = stack.top()
        if not expression[i].isnumeric():
            if expression[i] is ')':
                while stack.top().value is not '(':
                    queue.enqueue(stack.pop().value)
                stack.pop()
                i+=1
                continue
            elif (current is not None and
                 current.value is not '(' and
                 expression[i] is not '(' and
                current.precedence > find_precedence(expression[i])):
                queue.enqueue(stack.pop().value)
            stack.push(TokenType(expression[i]))
            i+=1
            continue
        while i < len(expression) and expression[i].isdigit():
            val*=10
            val+=int(expression[i])
            i+=1
        queue.enqueue(val)
    while not stack.is_empty():
        queue.enqueue(stack.pop().value)
    return queue

def eval_rpn(rpn:Queue) -> float:
    stack = Stack()
    res = 0
    while not rpn.is_empty():
        if str(rpn.head()).isnumeric():
            stack.push(rpn.dequeue())
        else:
            right = stack.pop()
            left = stack.pop()
            match rpn.head():
                case '+':
                    stack.push(int(left) + int(right))
                case '*':
                    stack.push(int(left) * int(right))
                case '-':
                    stack.push(int(left) - int(right))
                case '/':
                    stack.push(int(left) / int(right))
            rpn.dequeue()
    return stack.top()



