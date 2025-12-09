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
    def __init__(self,expression:str,i:int,left:int,right:int):
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
