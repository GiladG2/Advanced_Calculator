from Queue import Queue
from Stack import Stack
from TokenType import *
from Tokens import is_op, is_binary_op, is_valid_token, is_left_associative, is_unary_op
from exceptions import TildeException, InvalidCharacterException, UnopenedParenthesesException, \
    EmptyParenthesesException, FactorialException, DecimalOfDecimalException, IncorrectHashtagException


#returns if the previous token is a number
def prev_is_numeric(expression, i):
    return get_prev_token(expression, i).isnumeric()


#returns the previous token excluding ')'
def get_prev_token(expression, i):
    if i >= 1:
        if expression[i - 1] is ')':
            return expression[i - 2]
        return expression[i - 1]
    return expression[i]


#returns the previous token
def get_prev_token_including(expression, i):
    if i >= 1:
        return expression[i - 1]
    return expression[i]


#returns if there is a negation
def is_negation(expression, i: int):
    prev_token = get_prev_token(expression, i)
    return ((i == 0 or ((prev_token is not None
                        and (is_binary_op(prev_token)
                             or prev_token == '('
                             or prev_token is '~'))
             and not prev_is_numeric(expression, i))))


#returns if the syntax of a tilde is valid
def is_valid_tilde(stack, expression, i):
    return ((stack.is_empty() or (stack.top().value is not 'u' and stack.top().value is not 'w'))
    and not prev_is_numeric(expression, i))
def both_unary(token1,token2) -> bool:
    return is_unary_op(token1) and is_unary_op(token2)
#returns if both current and expression[i] are both valid operations
def check_enqueue_binary_op(current, expression, i):
    return (current is not None
            and (
                    (is_op(current.value) or current.value in ['u','w'])
                    and (is_op(expression[i]))
                    and not is_binary_op(expression[i - 1])
            and not is_negation(expression,i)))
def compare_op(current, expression, i):
    return ((current.precedence > find_precedence(expression[i])
             or (current.precedence == find_precedence(expression[i]))
                 and (both_unary(expression[i],current.value)
                      or is_left_associative(expression[i]))))
#handles implicit multiplication
def implicit_mul(stack: Stack, queue: Queue, i: int):
    if not stack.is_empty():
        if is_op(stack.top().value) and 2 <= stack.top().precedence:
            queue.enqueue(stack.pop())
    stack.push(TokenType('*', i))

#returns the next token
def get_next_token(expression, i):
    if i < len(expression) - 1:
        return expression[i + 1]
    return expression[i]


#returns True if the syntax of the factorial is incorrect
def incorrect_factorial(current_token, next_token):
    return (current_token is '!'
            and (next_token.isdigit()
                 or (next_token is not '!'
                     and (not is_binary_op(next_token) and next_token != ')'))))
def incorrect_hashtag(current_token, next_token):
    return (current_token is '#'
            and (next_token.isdigit()
                 or (next_token is not '#'
                     and (not is_binary_op(next_token) and next_token != ')'))))
def incorrect_unary(next_token):
    return (next_token.isdigit()
                 or ( not is_unary_op(next_token)
                     and (not is_binary_op(next_token) and next_token != ')')))
#recieves a mathematical expression and returns its post fix annotation
def expression_to_rpn(expression: str) -> Queue:
    stack = Stack()
    queue = Queue()
    i = 0
    while i < len(expression):
        #stack.info()
        if not is_valid_token(expression[i]):
            raise InvalidCharacterException(expression, i)
        next_token = get_next_token(expression, i)
        if expression[i] is '#' and incorrect_unary(next_token):
            raise IncorrectHashtagException(expression,i)
        if expression[i] is '!' and incorrect_unary(next_token):
            raise FactorialException(expression, i)
        current: TokenType | None = None
        if not stack.is_empty():
            current = stack.top()
        if not expression[i].isnumeric():
            if expression[i] is ')':
                if not stack.is_empty() and expression[i - 1] == '(':
                    raise EmptyParenthesesException(expression, i)
                while not stack.is_empty() and stack.top().value is not '(':
                    queue.enqueue(stack.pop())
                if stack.is_empty():
                    raise UnopenedParenthesesException(expression, i)
                stack.pop()
                i += 1
                if i < len(expression) and expression[i] is '(':
                    implicit_mul(stack, queue, i)
                continue
            elif ((check_enqueue_binary_op(current, expression, i)
                  and compare_op(current, expression, i))):
                if current.value == 'u' or current.value is 'w':
                    while( not stack.is_empty() and
                        (stack.top().value is 'u' or stack.top().value is 'w')):
                        queue.enqueue(stack.pop())
                else:
                    if not stack.is_empty() and is_op(stack.top().value):
                        queue.enqueue(stack.pop())
            if (expression[i] is '-' and
                    is_negation(expression, i)):
                if not stack.is_empty() and stack.top().value is 'w':
                    stack.push(TokenType('w', i))
                else:
                    stack.push(TokenType('u', i))
            elif expression[i] is '~':
                if is_valid_tilde(stack, expression, i):
                    stack.push(TokenType('w', i))
                else:
                    raise TildeException(expression, i)
            elif is_op(expression[i]) or expression[i] is ')' or expression[i] is '(':
                stack.push(TokenType(expression[i], i))
            i += 1
            continue
        prev_token = get_prev_token_including(expression, i)
        if prev_token is ')':
            implicit_mul(stack, queue, i)
        prev_token = get_prev_token(expression, i)
        val = 0
        mul = 0.1
        if prev_token == '.':
            if i>=2 and expression[i-2] == '.':
                raise DecimalOfDecimalException(expression, i-1)
            if i>=2 and expression[i-2] == ')':
               implicit_mul(stack,queue,i)
            while i < len(expression) and expression[i].isnumeric():
                val += mul * float(expression[i])
                mul *= 0.1
                i += 1
        if i < len(expression) and expression[i] is '.':
            raise DecimalOfDecimalException(expression, i)
        while i < len(expression) and expression[i].isdigit():
            val *= 10
            val += int(expression[i])
            i += 1
        if i < len(expression) and expression[i] is '.':
            i += 1
            while i < len(expression) and expression[i].isdigit():
                val += mul * float(expression[i])
                i += 1
                mul *= 0.1
        if i < len(expression) and expression[i] is '.':
            raise DecimalOfDecimalException(expression, i)
        queue.enqueue(val)

        if i < len(expression) and expression[i] is '(':
            implicit_mul(stack, queue, i)
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    return queue
