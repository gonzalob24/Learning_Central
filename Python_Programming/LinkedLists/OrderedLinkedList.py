from Node1 import Node


class OrderedList:
    """

    Implementing an ordered list

    """
    def __init__(self):
        self.start = None

    # The next three methods work the same as in the
    # Unordered Link List Class above

    def is_empty(self):
        return self.start is None

    def size(self):
        if self.start is None:
            print("The Ordered List is empty")

        p = self.start
        count = 0
        while p is not None:
            count += 1
            p = p.next
        return count

    def remove(self, item):
        prev = None
        p = self.start
        found = False

        while not found:
            if p.info == item:
                found = True
            else:
                prev = p
                p = p.next

        if prev is None:
            self.start = p.next
        else:
            prev.next = p.next

    def search(self, item):
        p = self.start
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

    def search2(self, data):
        return
        # code this tomorrow for warm up.

    def add(self, item):
        temp = Node(item)
        larger = False
        p = self.start
        prev = None

        while p is not None and not larger:
            if p.info > item:
                larger = True
            else:
                prev = p
                p = p.next
        if prev is None:
            temp.next = p
            self.start = temp
        else:
            temp.next = p
            prev.next = temp

    def insert_in_order(self, data):
        temp = Node(data)
        if self.start == None or data < self.start.info:
            temp.link = self.start
            self.start = temp
            return

        p = self.start
        while p.link is not None and p.link.info <= data:
            p = p.link

        temp.link = p.link
        p.link = temp

    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        else:
            print("The list is: ")
            p = self.start
            while p is not None:
                print(p.info, end=" ")
                p = p.next
            print()


if __name__ == '__main__':
    mylist2 = OrderedList()  # Its empty
    mylist2.add(1)
    mylist2.add(2)
    mylist2.add(18)
    mylist2.add(11)
    mylist2.add(5)
    mylist2.add(0)
    mylist2.display()
    print(mylist2.size())
