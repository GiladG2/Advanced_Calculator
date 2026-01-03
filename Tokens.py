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
def is_unary_op(token) -> bool:
    return (token == '!'
            or token is '#'
            or token is 'w'
            or token is 'u'
            or token is '~'
            or token is '-')
def is_op(token) -> bool:
    return (is_binary_op(token)
            or is_unary_op(token))
def is_valid_token(token) -> bool:
    return (token == '.'
            or token.isdigit()
            or is_op(token)
            or token == '('
            or token == ')'
            or token == '~')
def is_left_associative(token) -> bool:
    return not (token is '^')
class Token(Enum):
   _tokens = {1:['+','-'],2:['*','/'],2.5:['u'],3:['^'],4:['%'],
              5:['$','@','&'],6:['!','#','w']}



