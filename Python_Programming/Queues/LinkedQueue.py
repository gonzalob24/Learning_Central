# Class implementation of a queue


class EmptyQueueError(Exception):
    pass


class Node:

    def __init__(self, value):
        self.info = value
        self.link = None


class LinkedQueue:

    def __init__(self):
        self.front = None  # Reference to the front initialized to None
        self.rear = None   # Reference to the rear initialized to None
        self.size_queue = 0

    def is_empty(self):
        return self.front is None

    def size(self):
        return self.size_queue

    def enqueue(self, value):
        temp = Node(value)
        if self.front is None:
            self.front = temp
        else:
            self.rear.link = temp

        self.rear = temp
        self.size_queue += 1  # Every time a Node is added increment size_queue by 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        x = self.front.link  # The value being removed from the front
        self.front = self.front.link
        self.size_queue -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        return self.front.info

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("The Queue is: ")
        p = self.front
        while p is not None:
            print(p.info, end=" ")
            p = p.link


if __name__ == '__main__':
    qu = LinkedQueue()
    qu.enqueue(1)
    qu.enqueue(3)
    qu.enqueue(5)
    qu.display()

    # while True:
    #     print("1.Enqueue")
    #     print("2.Dequeue")
    #     print("3.Peek")
    #     print("4.Size")
    #     print("5.Display")
    #     print("6.Quit")

