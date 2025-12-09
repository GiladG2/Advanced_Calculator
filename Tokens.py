from enum import Enum
def is_left_associative(token) -> bool:
    if token is '+' or '-' or '*' or '/':
        return True
    return False
def is_op(token) -> bool:
    if (token == '+' or token == '-' or token == '*' or token == '/' or
          token == '@' or token == '$'
            or token == '^' or token == '%' or token == '&' or token == '~'):
        return True
    return False
def is_valid_token(token) -> bool:
    if (token is '(' or token is ')' or
    token is '!' or
            token.isdigit() or is_op(token)):
        return True
    return False

class Token(Enum):
   _tokens = {1:['+','-','u'],2:['*','/'],3:['^'],4:['%'],
              5:['$','@','&'],6:['!']}



