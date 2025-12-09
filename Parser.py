from Lexer import *
from exceptions import *
from Math_Func import __is_numeric__
from Queue import Queue
from Stack import Stack
from Math_Func import *

def evaluate(expression:str) -> float:
    try:
        res = eval_rpn(expression_to_rpn(expression),expression)
        return res
    except TildeException as e:
        print(e)
    except DivisionByZeroException as e:
        print(e)
    except InvalidBinaryOpException as e:
        print(e)
    except InvalidCharacterException as e:
        print(e)
    except EmptyExpressionException as e:
        print(e)
    except UnopenedParenthesesException as e:
        print(e)
    except UnclosedParenthesesException as e:
        print(e)
#gets an expression in post fix notation and evaluates it
def eval_rpn(rpn:Queue,expression:str) -> float:
    stack = Stack()
    while not rpn.is_empty():
        if __is_numeric__(str(rpn.head())):
            stack.push(rpn.dequeue())
        else:
                if rpn.head().value == '(':
                    raise UnclosedParenthesesException(expression,rpn.head().index)
                right = stack.pop()
                if rpn.head().value is 'u':
                    stack.push(right*-1)
                    rpn.dequeue()
                    continue
                if rpn.head().value is '!':
                    stack.push(fac(right))
                    rpn.dequeue()
                    continue
                if stack.is_empty():
                    raise InvalidBinaryOpException(expression,rpn.head().index)
                left = stack.pop()
                match rpn.head().value:
                    case '+':
                        stack.push(int(left) + int(right))
                    case '*':
                        stack.push(int(left) * int(right))
                    case '-':
                        stack.push(int(left) - int(right))
                    case '/':
                        if right == 0:
                            raise DivisionByZeroException(expression,rpn.head().index,left,right)
                        stack.push(int(left) / int(right))
                    case '^':
                        stack.push(int(left) ** int(right))
                    case '%':
                        stack.push(int(left) % int(right))
                    case '$':
                        stack.push(max(int(left), int(right)))
                    case '&':
                        stack.push(min(int(left), int(right)))
                    case '@':
                        stack.push(average(int(left), int(right)))
                rpn.dequeue()
    if stack.is_empty():
        raise EmptyExpressionException(expression)
    return stack.top()