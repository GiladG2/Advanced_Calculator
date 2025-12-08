from Queue import Queue
from Stack import Stack
from TokenType import *
from Tokens import is_op
#gets the expression and turns its annotation to post fix
def expression_to_rpn(expression: str) -> Queue:
    stack = Stack()
    queue = Queue()
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i+=1
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
            elif (current is not None and
                  current.value is not '(' and
                  expression[i] is not '(' and
                  not is_op(expression[i-1]) and
                  current.precedence >= find_precedence(expression[i])
            ):
                queue.enqueue(stack.pop().value)
            if ((expression[i] is '-' or expression[i] is '~') and(
                    i==0 or is_op(expression[i - 1]) or
                    expression[i-1] == '(')):
                stack.push(TokenType('u'))
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
