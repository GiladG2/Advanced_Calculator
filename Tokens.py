from enum import Enum
def is_binary_op(token) -> bool:
    return (token == '+'
            or token == '-'
            or token == '*'
            or token == '/'
            or token == '@'
            or token == '$'
            or token == '^'
            or token == '%'
            or token == '&')
def is_op(token) -> bool:
    return (is_binary_op(token)
            or token == '!'
            )
def is_valid_token(token) -> bool:
    return (token == '.'
            or token.isdigit()
            or is_op(token)
            or token == '('
            or token == ')'
            or token == '~')

class Token(Enum):
   _tokens = {1:['+','-','u'],2:['*','/'],3:['^'],4:['%'],
              5:['$','@','&'],6:['!']}



