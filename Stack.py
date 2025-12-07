from Node import *
class Stack:
    def __init__(self):
            self.head : Node | None  = None
    def top(self):
        return self.head.value
    def is_empty(self):
        return self.head is None

    def push(self, val):
        dummy : Node = Node(val)
        dummy.next = self.head
        self.head = dummy
    def pop(self):
        val = self.head.value
        self.head = self.head.next
        return val

