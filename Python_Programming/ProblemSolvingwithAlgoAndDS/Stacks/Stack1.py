"""
Creating the class Stack to implement instances of the class Stack\
"""


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):  # Adds item to the top of the stack
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.size() - 1]

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
    revstring(strng)

