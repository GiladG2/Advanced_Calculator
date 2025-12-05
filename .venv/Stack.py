from Node import *
from Tokens import *
class Stack:
    def __init__(self):
            self.top : Node  = None
    def top(self):
        return self.top.value
    def is_empty(self):
        return self.top == None
    def push(self, val):
        dummy : Node = Node()
        dummy.value = val
        dummy.next = self.top
        self.top = dummy
    def pop(self):
        val = self.top.value
        self.top = self.top.next
        return val

