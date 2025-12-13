from TokenType import *
from Node import *


class Stack:
    def __init__(self):
        self.head: Node | None = None

    def top(self):
        return self.head.value

    def is_empty(self):
        return self.head is None

    def push(self, val):
        dummy: Node = Node(val)
        dummy.next = self.head
        self.head = dummy

    def pop(self):
        val = self.head.value
        self.head = self.head.next
        return val
    def info(self):
        stack2 = Stack()
        while not self.is_empty():
            if isinstance(self.top(),TokenType):
                print(self.top().value)
            else:
                print(self.top())
            stack2.push(self.pop())
        while not stack2.is_empty():
            self.push(stack2.pop())