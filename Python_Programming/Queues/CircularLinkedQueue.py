# Circular implementation of a Queue


class EmptyQueueError(Exception):
    pass


class Node:

    def __init__(self, value):
        self.info = value
        self.link = None


class CircularLinkedQueue:

    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear is None

    def size(self):
        if self.is_empty():
            return 0

        count = 0
        p = self.rear.link
        while True:
            count += 1
            p = p.link
            if p == self.rear.link:
                break

        return count

    def enqueue(self, value):
        temp = Node(value)
        if self.is_empty():
            self.rear = temp
            self.rear.link = self.rear
        else:
            temp.link = self.rear.link
            self.rear.link = temp
            self.rear = temp

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        if self.rear.link == self.rear:  # The queue only has one element
            temp = self.rear
            self.rear is None
        else:
            temp = self.rear.link
            self.rear.link = temp.link

        return temp.info

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        return self.rear.link.info

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Que is: ")

        p = self.rear.link
        while True:
            print(p.info, end=" ")
            p = p.link
            if p == self.rear.link:
                break


if __name__ == '__main__':
    que = CircularLinkedQueue()
    que.enqueue(4)
    que.enqueue(3)
    que.enqueue(34)
    que.enqueue(14)
    que.enqueue(24)
    que.display()
    # while True:
    #     print("1.Enque")
    #     print("2.Dequeue")
    #     print("3.Peek")
    #     print("4.Size")
    #     print("5.Display")
    #     print("6.Quit")


