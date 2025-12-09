from Tokens import Token


def find_precedence(token) -> int | None:
    dict = Token._tokens
    for i in dict.value:
        if token in dict.value[i]:
            return i
    return None


def has_left_association(token):
    if token == '+' or token == '-' or token == '*' or token == '/':
        return True
    return False


class TokenType:
    def __init__(self, token,index):
        self.value = token
        self.precedence = find_precedence(token)
        self.index = index
