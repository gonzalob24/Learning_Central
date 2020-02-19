# Class for a queue


class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(3)
    q.display()
    print(q.size())
    q.enqueue("doggy")
    q.display()
    print(q.size())
