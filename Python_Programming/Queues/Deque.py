# Creating a class to create deques
# Deque demonstrates behavior of Queues and Stacks
# Its a double ended Queue


class EmptyQueueError(Exception):
    pass


class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):  # This is not the most efficient way
        self.items.insert(0, item)

    def add_rear(self, item):   # This is not the most efficient way
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items.pop()

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items[0]

    def last(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


if __name__ == '__main__':
    d = Deque()
    print(d.is_empty())
    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    print(d.remove_rear())
    print(d.remove_front())
    d.display()
