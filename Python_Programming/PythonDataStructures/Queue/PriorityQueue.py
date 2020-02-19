class EmptyQueueError(Exception):
    pass


class Node:

    def __init__(self, value, pr):
        self.info = value
        self.priority = pr
        self.link = None


class PriorityQueue:

    def __init__(self):
        self.front = None

    def enqueue(self, data, data_priority):  # Add node to queue
        temp = Node(data, data_priority)

        # If queue is empty or element to be added has priority more than first element
        if self.is_empty() or data_priority  < self.front.priority:
            temp.link - self.front
            self.front = temp
        else:
            p = self.front
            while p.link is not None and p.link.priority <= data_priority:
                p = p.link
            temp.link = p.link
            p.link = temp

    def dequeue(self):   # Delete Node
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        x1 = self.front.info
        self.front = self.front.link
        return x1

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        print("Queue is: ")
        p = self.front
        while p is not None:
            print(p.info, " ", p.priority)
            p = p.link
        print()

    def size(self):
        n = 0
        p = self.front
        while p is not None:
            n += 1
            p = p.link
        return n


if __name__ == "__main__":
    qu = PriorityQueue()   # I can add up to 10 elements since 10 is tha max size

    while True:
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display all queue elements")
        print("4. Display size of the queue")
        print("5. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            x = int(input("Enter the element: "))
            pr = int(input("Enter its priority: "))
            qu.enqueue(x, pr)
        elif choice == 2:
            x = qu.dequeue()
            print("Element is: ", x)
        elif choice == 3:
            qu.display()
        elif choice == 4:
            print("Sie of Queue is: ", qu.size())
        elif choice == 5:
            break
        else:
            print("Wrong choice")
        print()
