class EmptyQueueError(Exception):
    pass


class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def insert_front(self, item):  # Done in constant time
        self.items.insert(0, item)

    def insert_rear(self, item):   # Shifting of elements
        self.items.append(item)

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.items.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items.pop()

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue us Empty")
        return self.items[0]

    def last(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items[-1]

    def display(self):
        print(self.items)


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
