# A linked implementation of a deque
# reference to thr front and rear of the queue
# adding and deleting can be performed in constant time


class EmptyStackError(Exception):
    pass


class Node:

    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None


class LinkedDeque:

    # Initially front and rear will be null
    def __init__(self):
        self.front = None
        self.rear = None

    # adds item to the front of the deque
    def add_front(self, item):
        temp = Node(item)
        if self.is_empty():
            self.front = self.rear = temp
        else:
            temp.next = self.front
            self.front.prev = temp
            self.front = temp

    # add item at the rear of the deque
    def add_rear(self, item):
        temp = Node(item)
        if self.is_empty():
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear
            self.rear = temp

    # display the contents of the dequeue
    def display(self):
        p = self.front
        while p is not None:
            print(p.info, end=" ")
            p = p.next
        print("\n")
    # display items using recursion with a helper function
    def _display_recursion(self, p):
        if p.next is None:
            print(p.info)
        else:
            print(p.info, end=" ")
            self._display_recursion(p.next)

    def display_recursively(self):
        self._display_recursion(self.front)

    # Delete a node from the front
    def delete_front(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")

        front_item = self.front.info
        if self.front.next is None:  # Deque has only one item
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None

        return front_item

    # delete item from the rear
    def delete_rear(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")

        rear_item = self.rear.info  # this is the last item in the deque
        if self.front.next is None: # Deque has only one item in the list
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None

        return rear_item

    # Check if the double ended queue is empty
    def is_empty(self):
        return self.front is None

    def size_iteration(self):
        count = 0
        p = self.front   # p is a reference to the first node
        while p is not None:
            count += 1
            p = p.next
        return count

    def _size_recursion(self, p):
        if p.next is None:
            return 1
        else:
            return 1 + self._size_recursion(p.next)

    def size_recursion(self):
        return self._size_recursion(self.front)  # use self.front to refer to the first nodes

    # Get the first item from the deque
    def first(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")

        return self.front.info

    # Get the last item
    def last(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")

        return self.rear.info

if __name__ == '__main__':
    d1 = LinkedDeque()
    d1.add_front(4)
    d1.add_front(43)
    d1.add_front(17)
    d1.add_front(45)
    d1.add_rear(76)
    size1 = d1.size_iteration()
    size2 = d1.size_recursion()
    print("Size using iteration: ", size1)
    print("Size using recursion: ", size2)
    d1.display()
    d1.display_recursively()
    d1.delete_front()
    d1.display()
    d1.delete_rear()
    d1.display()
    print("First item: ", d1.first())
    print("Last item: ", d1.last())
