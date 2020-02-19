# This implementation is very similar as a circular que
# Circular implementation of a deque
# insertion and deletion are order of 1
#

class EmptyQueueError(Exception):
    pass


class Deque:

    def __init__(self, default_size=10):
        self.items = [None] * default_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def insert_front(self, item):
        if self.count == len(self.items):
            self.resize(2 * len(self.items))

        self.front = (self.front - 1) % len(self.items)
        self.items[self.front] = item
        self.count += 1

    def insert_rear(self, item):
        if self.count == len(self.items):
            self.resize(2 * len(self.items))

        i = (self.front + self.count) % len(self.items)
        self.items[i] = item
        self.count += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        x = self.items[self.fron]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1

        return x

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        rear = (self.front + self.count - 1) % len(self.items)
        x = self.items[rear]
        self.items[rear] = None
        self.count -= 1
        return x

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        return self.items[self.front]

    def last(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        rear = (self.front + self.count - 1) % len(self.items)
        return self.items[rear]

    def display(self):
        print(self.items)

    def resize(self, newsize):
        old_list = self.items
        self.items = [None] * newsize
        i = self.front

        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (1 + i) % len(old_list)

        self.front = 0





