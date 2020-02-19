# Implementation of a Queue using an array
# There si some work to be done because the elements
# shift every time I dequeue.


class EmptyStackError(Exception):
    pass


class Queue:

    def __init__(self):
        self.items = []  # Initialize an empty stack

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):  # This part of the code can be improved due to shifting of elements
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")

        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")
        return self.items(0)

    def display(self):
        print(self.items)
