# Improved Implementation of a Queue using an array
# But still needs more work because of the wasted memory to add None
#


class EmptyStackError(Exception):
    pass


class Queue:

    def __init__(self):
        self.items = []  # Initialize an empty stack
        self.front = 0

    def is_empty(self):
        return self.front == len(self.items)

    def size(self):
        return len(self.items) - self.front

    def enqueue(self, item):
        self.items.append(item)

    # Improved dequeue but it is still inefficient because of the unnecessary waste of memory
    # because it replaces value with None
    def dequeue(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")

        x = self.items[self.front]
        self.items[self.front] = None
        self.front += 1

        return x

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")

        return self.items[self.front]

    def display(self):
        print(self.items)


myQ = Queue()
myQ.enqueue(1)
myQ.enqueue(2)
myQ.enqueue(3)
myQ.enqueue(4)
print("The size of the queue is: ", myQ.size())
myQ.display()
myQ.dequeue()
myQ.dequeue()
myQ.display()
print("The size of the queue is: ", myQ.size())

