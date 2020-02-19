from Node1 import Node


class UnorderedLinkedList:

    def __init__(self):
        self.head = None  # Must reference the start of the list

    def is_empty(self):
        return self.head is None

    # Adding will always be O(1) for unsorted list
    def add_at_head(self, item):  # Easiest place to add a  node is in the head
        temp = Node(item)  # Create a temp Node to be linked or added
        temp.next = self.head  # same as temp.self_next(self.head)
        self.head = temp

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

    def size(self):
        count = 0
        p = self.head
        while p is not None:
            count += 1
            p = p.next
        return count

    def search(self, item):
        p = self.head
        position = 1
        # found = False

        while p is not None:
            if p.info == item:
                print(item, ' is at position ' ,position)
                return True  # Exits the loop otherwise we will be in never ending loop
            else:
                p = p.next
                position += 1

    def remove(self, item):
        p = self.head
        found = False
        prev = None

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

    def append(self, item):
        if self.head is None:
            self.head = Node(item)
            return

        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(item)

    # def insert(self):

    # def index(self):

    # def pop(self):


if __name__ == '__main__':
    mylist = UnorderedLinkedList()
    mylist.add_at_head(93)
    mylist.add_at_head(11)
    mylist.add_at_head(1)
    mylist.add_at_head(2)
    mylist.add_at_head(7)
    mylist.display()
    print("The current count of my list is ", mylist.size())
    print(mylist.search(2))
    mylist.remove(7)
    mylist.display()

    mylist = UnorderedLinkedList()
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    mylist.display()
