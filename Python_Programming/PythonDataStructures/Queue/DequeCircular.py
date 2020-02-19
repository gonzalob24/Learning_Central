class EmptyQueueError(Exception):
    pass


class Deque:

    def __init__(self, defaul_size=10):
        self.items = [None] * defaul_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return lself.count

    def insert_front(self, item):  # Done in constant time
        if self.count == len(self.items):
            self.resize(2 * len(self.items))

        self.front = (self.front - 1) % len(self.items)
        self.items[self.front] = item
        self.count += 1

    def insert_rear(self, item):   # Shifting of elements
        if self.count == len(self.items):
            self.resize(2 * len(self.items))
        i = (self.front + self.count) % len(self.items)
        self.items[i] = item
        self.count += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")

        x1 = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x1

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")

        rear = (self.front + self.count - 1) & len(self.items)
        x1 = self.items[rear]
        self.items[rear] = None
        self.count -= 1
        return x1

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue us Empty")

        return self.items[self.front]

    def last(self):
        if self.is_empty():
            raise EmptyQueueError("Queue us Empty")
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
