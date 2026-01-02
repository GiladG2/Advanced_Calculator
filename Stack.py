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
        l = []
        stack2 = Stack()
        while not self.is_empty():
            if isinstance(self.top(),TokenType):
                l.append(self.top().value)
            else:
                l.append(self.top())
            stack2.push(self.pop())
        while not stack2.is_empty():
            self.push(stack2.pop())
        print(l)