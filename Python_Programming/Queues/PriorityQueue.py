# Implementation of a priority queue


class EmptyQueueError(Exception):
    pass


class Node:
    def __init__(self, value, priority):
        self.info = value
        self.priority = priority
        self.link = None


class PriorityQueue:

    def __init__(self):
        self.front = None  # refers to the first node of the list

    def is_empty(self):
        return self.front is None

    def enqueue(self, data, data_priority):
        temp = Node(data, data_priority)

        # If Queue is empty or priority of new element is more than first element
        if self.is_empty() or data_priority < self.front.priority:
            temp.link = self.front
            self.front = temp
        else:
            p = self.front
            while p.link is not None and p.link.priority <= data_priority:
                p = p.link

            temp.link = p.link
            p.link = temp

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        x = self.front.info
        self.front = self.front.link
        return x  # The value that is being removed from the front

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Que is: ")
        p = self.front
        while p is not None:
            print(p.info, "\twith priority ", p.priority)
            p = p.link
        print()

    def size(self):
        count = 0
        p = self.front
        while p is not None:
            count += 1
            p = p.link
        return count

pr = PriorityQueue()
pr.enqueue(1, 1)
pr.enqueue(2, 3)
pr.enqueue(10, 2)
pr.display()
