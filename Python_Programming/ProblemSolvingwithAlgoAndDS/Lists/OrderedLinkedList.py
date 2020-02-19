from Node1 import Node


class OrderedList:
    """

    Implementing an ordered list

    """
    def __init__(self):
        self.head = None

    # The next three methods work the same as in the
    # Unordered Link List Class above

    def is_empty(self):
        return self.head is None

    def size(self):
        if self.head is None:
            print("The Ordered List is empty")

        p = self.head
        count = 0
        while p is not None:
            count += 1
            p = p.next

    def remove(self, item):
        prev = None
        p = self.head
        found = False

        while not found:
            if p.info == item:
                found = True
            else:
                prev = p
                p = p.next

        if prev is None:
            self.head = p.next
        else:
            prev.next = p.next

    def search(self, item):
        p = self.head
        found = False
        large = False

        while p is not None and not large and not found:
            if p.info == item:
                found = False
                print(p.info, " is in the list")
            elif p.info > item:
                large = True
                print(p.info, " is large than ", item, " the number is not in the list")
            else:
                p = p.next

    def add(self, item):
        temp = Node(item)
        larger = False
        p = self.head
        prev = None

        while p is not None and not larger:
            if p.info > item:
                larger = True
            else:
                prev = p
                p = p.next
        if prev is None:
            self.head = temp
        else:
            temp.next = p
            prev.next = temp

    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        else:
            print("The list is: ")
            p = self.head
            while p is not None:
                print(p.info, end=" ")
                p = p.next
            print()

    def predecessor_of_node(self, x):
        p = self.head
        # prev = None  will not be using a previous holder
        position = 1  # Change position to 1
        while p.next is not None:  # Make sure that the link is not None
            if p.next.info == x:
                print(p.info, " is at position, ", position)
            position += 1
            # prev = p
            p = p.next


if __name__ == '__main__':
    mylist2 = OrderedList()  # Its empty
    mylist2.add(1)
    mylist2.add(2)
    mylist2.add(18)
    mylist2.add(11)
    mylist2.add(5)
    mylist2.add(3)
    mylist2.display()
    mylist2.predecessor_of_node(11)
