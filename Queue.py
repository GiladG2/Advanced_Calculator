from Node import *


class Queue:
    def __init__(self):
        self.first: Node = None
        self.last: Node = None

    def is_empty(self) -> bool:
        return self.first is None

    def enqueue(self, value):
        if self.is_empty():
            self.first = Node(value)
            self.last = self.first
        else:
            self.last.next = Node(value)
            self.last = self.last.next

    def dequeue(self):
        val = self.first.value
        self.first = self.first.next
        return val

    def head(self):
        return self.first.value
