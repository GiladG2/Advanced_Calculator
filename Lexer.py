from Queue import Queue
from Stack import Stack
from TokenType import *
from Tokens import is_op
from exceptions import TildeException


#gets the expression and turns its annotation to post fix
def prev_is_numeric(expression, i):
    i -= 1
    while i >= 0:
        if expression[i].isdigit():
            return True
        i = -1
    return False

def is_negation(prev, i: int):
    if  i == 0 or prev is not None or is_op(prev) or prev == '(':
        return True
    return False
def binary_op(current,expression,i):
    return(current is not None and
    current.value is not '(' and
    expression[i] != '~' and
    expression[i] is not '(' and
    not is_op(expression[i - 1]))


def expression_to_rpn(expression: str) -> Queue:
    stack = Stack()
    queue = Queue()
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        val = 0
        current: TokenType | None = None
        if not stack.is_empty():
            current = stack.top()
        if not expression[i].isnumeric():
            if expression[i] is ')':
                while stack.top().value is not '(':
                    queue.enqueue(stack.pop().value)
                stack.pop()
                i += 1
                continue
            elif (binary_op(current,expression,i) and
                  current.precedence >= find_precedence(expression[i])
            ):
                queue.enqueue(stack.pop().value)
                while not stack.is_empty() and stack.top().value is 'u':
                    queue.enqueue(stack.pop().value)
            if (expression[i] is '-' and
                    is_negation(expression[i - 1], i)):
                stack.push(TokenType('u'))
            elif expression[i] is '~':
                if ((stack.is_empty() or stack.top().value is not 'u')
                and prev_is_numeric(expression, i) == False):
                    stack.push(TokenType('u'))
                else:
                    raise TildeException(expression, i)
            else:
                stack.push(TokenType(expression[i]))
            i += 1
            continue
        while i < len(expression) and expression[i].isdigit():
            val *= 10
            val += int(expression[i])
            i += 1
        queue.enqueue(val)
    while not stack.is_empty():
        queue.enqueue(stack.pop().value)
    return queue
