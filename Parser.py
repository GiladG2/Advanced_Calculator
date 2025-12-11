from math import factorial

from Lexer import *
from exceptions import *
from Math_Func import __is_numeric__
from Queue import Queue
from Stack import Stack
from Math_Func import *

def evaluate(expression:str) -> float:
    try:
        expression = expression.replace(" ","")
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
    except EmptyParenthesesException as e:
        print(e)
    except FactorialException as e:
        print(e)
    except NoNumbersException as e:
        print(e)
    except NegativeFactorialException as e:
        print(e)
    except ModuloByZeroException as e:
        print(e)
    except ZeroToNegativePowerException as e:
        print(e)
    except DecimalOfDecimalException as e:
        print(e)
    except FactorialOfDecimalException as e:
        print(e)
    except OverflowUnaryException as e:
        print(e)
    except OverflowBinaryException as e:
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
                if stack.is_empty():
                    raise NoNumbersException(expression,rpn.head().index)
                right = stack.pop()
                if rpn.head().value is 'u':
                    stack.push(right*-1)
                    rpn.dequeue()
                    continue
                if rpn.head().value is '!':
                    if right <0:
                        raise NegativeFactorialException(expression,rpn.head().index,right)
                    elif int(right) != right:
                        raise FactorialOfDecimalException(expression,rpn.head().index,right)
                    try:
                        stack.push(fac(int(right)))
                    except OverflowError:
                        raise OverflowUnaryException(expression,rpn.head().index,right)
                    rpn.dequeue()
                    continue
                if stack.is_empty():
                    raise InvalidBinaryOpException(expression,rpn.head().index)
                left = stack.pop()
                try:
                    match rpn.head().value:
                        case '+':
                                stack.push(float(left) + float(right))
                        case '*':
                            stack.push(float(left) * float(right))
                        case '-':
                             stack.push(float(left) - float(right))
                        case '/':
                            if right == 0:
                                raise DivisionByZeroException(expression,rpn.head().index,left,right)
                            stack.push(float(left) / float(right))
                        case '^':
                            if left == 0 and right<0:
                                raise ZeroToNegativePowerException(expression,rpn.head().index,left,right)
                            stack.push(float(left) ** float(right))
                        case '%':
                            if right == 0:
                                raise ModuloByZeroException(expression,rpn.head().index,left,right)
                            stack.push(float(left) % float(right))
                        case '$':
                            stack.push(max(float(left), float(right)))
                        case '&':
                            stack.push(min(float(left), float(right)))
                        case '@':
                            stack.push(average(float(left), float(right)))
                except   OverflowError:
                    raise OverflowBinaryException(expression,rpn.head().index,left,rpn.head().value,right)
                rpn.dequeue()
    if stack.is_empty():
        raise EmptyExpressionException(expression)
    return stack.top()