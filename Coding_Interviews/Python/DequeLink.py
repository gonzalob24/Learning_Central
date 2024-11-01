class EmptyQueueError(Exception):
    pass


class Node:

    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None


class Deque:

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        p = self.front
        while p is not None:
            count += 1
            p = p.next
        return count

    def insert_front(self, item):
        temp = Node(item)
        if self.is_empty():
            self.front = self.rear = temp
        else:
            temp.next = self.front
            self.front.prev = temp
            self.front = temp

    def insert_rear(self, item):
        temp = Node(item)
        if self.is_empty():
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear

        self.rear = temp

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        x = self.front.info
        if self.front.next is None:   # List has only one node
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        return x

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")

        x = self.rear.info
        if self.front.next is None:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return x

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.front.info

    def last(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.rear.info

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack is: ")
        p = self.top
        while p is not None:
            print(p.info, end=" ")
            p = p.link


if __name__ == "__main__":
    qu = Deque()   # I can add up to 10 elements since 10 is tha max size

    while True:
        print("1. Insert at the front end")
        print("2. Insert at the rear end")
        print("3. Delete from the front end")
        print("4. Delete from the front end")
        print("5. Display first element")
        print("6. Display last element")
        print("7. Display")
        print("8. Size")
        print("9. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            x = int(input("Enter the element: "))
            qu.insert_front(x)
        elif choice == 2:
            x = int(input("Enter the element: "))
            qu.insert_rear(x)
        elif choice == 3:
            x = qu.delete_front()
            print("Element deleted from the front is: ", x)
        elif choice == 4:
            x = qu.delete_rear()
            print("Element deleted from the front is: ", x)
        elif choice == 5:
            print("First element is ", qu.first())
        elif choice == 6:
            print("Last element is: ", qu.last())
        elif choice == 7:
            qu.display()
        elif choice == 8:
            print("Size of queue is: ", qu.size())
        elif choice == 9:
            break
        else:
            print("Wrong choice")
        print()
