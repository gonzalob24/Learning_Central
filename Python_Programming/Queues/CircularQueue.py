# The most improved version of a queue using modular division
# self.front keeps index of element
# self.count keeps track of number of elements in the queue


class EmptyStackError(Exception):
    pass


class CircularQueue:

    def __init__(self, default_size=10):
        self.items = [None] * default_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, item):
        if self.count == len(self.items):  # This means its full
            self.resize(2 * len(self.items))  # We have to increase the size

        i = (self.front + self.count) % len(self.items)  # Index of element
        self.items[i] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")

        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)  # front only changes when we remove items
        self.count -= 1

        return x

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")

        return self.items[self.front]

    def resize(self, newsize):
        old_list = self.items
        self.items = [None] * newsize
        i = self.front

        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (i + 1) % len(old_list)

        self.front = 0

    def display(self):
        print(self.items)


cq = CircularQueue()

cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(1)
cq.enqueue(55)
cq.enqueue(6)
print(cq.peek())
cq.display()
