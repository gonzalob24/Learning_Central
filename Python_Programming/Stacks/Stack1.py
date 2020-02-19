"""
Creating the class Stack to implement instances of the class Stack\
"""


class EmptyStackError(Exception):
    pass


class Stack:

    def __init__(self):  # Constructor
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):  # Adds item to the top of the stack
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return EmptyStackError("Stack is empty")

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[-1]  # OR self.items[len(self.items) - 1] or self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


strng = 'apple'
first = Stack()


def revstring(mystr):
    for i in range(len(mystr)):
        first.push(mystr[i])
    for i in range(len(mystr)):
        print(first.pop(), end='')


if __name__ == '__main__':
    first.push(3)
    first.push(4)
    first.push(1)
    first.push(12)
    first.display()
    x = first.peek()
    print("The peeked value is",x)


