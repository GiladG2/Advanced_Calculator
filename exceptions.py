class CalculatorException(Exception):
    def __init__(self, expression,i,msg):
        self.expression = expression
        self.i = i
        self.msg = msg
    def __str__(self):
        return (self.expression + "\n" +
                " " * self.i + "^\n"
                + " " * self.i + "| " + self.msg)

class TildeException(CalculatorException):
    def __init__(self,expression:str,i:int):
        super().__init__(expression,i,"Incorrect use of tilde\n Tilde should start negation and is left-associative\n e.g ~-3 = 3")
class DivisionByZeroException(CalculatorException):
    def __init__(self,expression:str,i:int,left:float,right:float):
        super().__init__(expression,i,f"Attempt to divide by zero\n {left}/{right}")
class InvalidBinaryOpException(CalculatorException):
    def __init__(self,expression:str,i:int):
        super().__init__(expression,i,f"Missing operand at binary operation")
class InvalidCharacterException(CalculatorException):
    def __init__(self,expression:str,i:int):
        super().__init__(expression,i,f"Invalid character\n Allowed only mathematical operations and numbers")
class EmptyExpressionException(CalculatorException):
    def __init__(self,expression:str):
        super().__init__(expression,0,"Mathematical expressions cannot be empty")
class UnopenedParenthesesException(CalculatorException):
    def __init__(self,expression:str,i:int):
        super().__init__(expression,i,"Unopened parentheses")
class UnclosedParenthesesException(CalculatorException):
    def __init__(self,expression:str,i:int):
        super().__init__(expression,i,"Unclosed parentheses")
class EmptyParenthesesException(CalculatorException):
    def __init__(self,expression:str,i:int):
        super().__init__(expression,i,"Parentheses cannot be empty")
class FactorialException(CalculatorException):
    def __init__(self,expression:str,i:int):
        super().__init__(expression,i,"Incorrect use of factorial \n Factorial should be right to a number \n and cannot be used as a binary operator")
class NoNumbersException(CalculatorException):
    def __init__(self,expression:str,i:int):
        super().__init__(expression,i,"Mathematical expressions have to contain numbers")
class NegativeFactorialException(CalculatorException):
    def __init__(self,expression:str,i:int,val):
        super().__init__(expression,i,f"Attempt to calculate factorial of a negative => ({val})!")
class ModuloByZeroException(CalculatorException):
    def __init__(self,expression:str,i:int,left:float,right:float):
        super().__init__(expression,i,f"Attempt to modulo by zero {left}%{right}")
class ZeroToNegativePowerException(CalculatorException):
    def __init__(self,expression:str,i:int,left:float,right:float):
        super().__init__(expression,i,f"Attempt to raise 0 to a negative power {left}^{right}")
class DecimalOfDecimalException(CalculatorException):
    def __init__(self,expression:str,i:int):
        super().__init__(expression,i,"Too many decimal dots")
class FactorialOfDecimalException(CalculatorException):
    def __init__(self,expression:str,i:int,val:float):
        super().__init__(expression,i,f"Factorial of a decimal number is undefined ({val}!)")
class OverflowUnaryException(CalculatorException):
    def __init__(self,expression:str,i:int,val,op):
        super().__init__(expression,i,f"Overflow exceeded, {val}{op} is too large ")
class OverflowBinaryException(CalculatorException):
    def __init__(self,expression:str,i:int,left:float,op:str,right:float):
        super().__init__(expression,i,f"Overflow exceeded, {left}{op}{right} is too large")