# The following is an implementation of a linked stack
class EmptyStackError(Exception):
    pass


class Node:

    def __init__(self, value):
        self.info = value
        self.link = None


class LinkedStack:

    def __init__(self):
        self.top = None  # Initialize the stack

    def is_empty(self):
        return self.top is None

    def size(self):
        if self.top is None:
            return 0

        count = 0
        p = self.top
        while p is not None:
            count += 1
            p = p.link

        return count

    def push(self, item):
        temp = Node(item)

        if self.top is None:
            self.top = temp
            return

        temp.link = self.top
        self.top = temp

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")

        popped = self.top.info
        self.top = self.top.link
        return popped

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")

        return self.top.info

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return

        print("Stack is: ")
        p = self.top
        while p is not None:
            print(p.info, end=' ')
            p = p.link
        print()


if __name__ == '__main__':
    stack1 = LinkedStack()
    stack1.push(10)
    stack1.push(11)
    stack1.push(1)
    stack1.display()
    stack1.pop()
    stack1.display()
