# Double Linked List

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


"""
class Node(object):

    def __init__(self, value):
        self.info = value
        self.next = None  # The next link that refers to info in next node
        self.prev = None  # The prev link that refers to info in the prev node


class DoubleLinkedList(object):

    def __init__(self):
        self.start = None  # Always refers to the first node of the list

    def display_list(self):  # Display is the same as int the SLL
        if self.start is None:
            print("List is empty")
            return

        print("List is : ")
        p = self.start
        while p is not None:
            print(p.info, " ", end='')
            p = p.next
        print()

    def insert_in_beginning(self, data):
        temp = Node(data)

        if self.start is None:
            self.insert_in_empty_list(data)
            return

        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert_in_empty_list(self, data):
        temp = Node(data)
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def create_list(self):
        n = int(input("Enter the number of Nodes: "))
        if n == 0:
            return

        data = int(input("Enter the first element to be inserted : "))
        self.insert_in_empty_list(data)

        for i in range(n - 1):
            data = int(input("Enter the next element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        temp = Node(data)
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next

        if p is None:
            print(x, " not present in the list")
        else:
            temp.prev = p
            temp.next = p.next
            if p.next is not None:
                p.next.prev = temp  # Should not be done when p refers to last Node
            p.next = temp

    def insert_before(self, data, x):
        if self.start is None:
            print("List is empty")
            return

        if self.start.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
            return

        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next

        if p is None:
            print(x, " not present in the list")
        else:
            temp = Node(data)
            temp.prev = p.prev
            temp.next = p
            p.prev.next = temp
            p.prev = temp

    def delete_first_node(self):
        if self.start is None:
            return  # List is empty
        if self.start.next is None:  # List has only one node
            self.start = None
            return
        self.start = self.start.next
        self.start.prev = None

    def delete_last_node(self):
        if self.start is None:
            return  # List is empty
        if self.start.next is None:
            self.start = None
            return

        p = self.start
        while p.next is not None:
            p = p.next
        p.prev.next = None

    def delete_node(self, x):
        if self.start is None:
            return  # List is empty
        if self.start.next is None:  # List has only one node
            if self.start.info == x:
                self.start = None
            else:
                print(x, " not found")
            return

        # Delete first node
        if self.start.info == x:
            self.start = self.start.next
            self.start.prev = None
            return

        p = self.start.next
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        if p.next is not None: # Node to be deleted is in between
            p.prev.next = p.next
            p.next.prev = p.prev
        else:  # p refers to last node
            if p.info == x:    # Node to be deleted is last node
                p.prev.next = None
            else:
                print(x, " not found")

    def reverse_list(self):
        if self.start is None:
            return

        p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.start = p1


l1 = DoubleLinkedList()
l1.insert_in_beginning(1)
l1.insert_at_end(3)
l1.insert_at_end(5)
l1.insert_at_end(2)
l1.insert_at_end(10)
l1.display_list()
l1.delete_last_node()
l1.delete_node(5)
l1.display_list()

