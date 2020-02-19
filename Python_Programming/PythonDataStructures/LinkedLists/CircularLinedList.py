class Node(object):

    def __init__(self, value):
        self.info = value
        self.link = None


class CircularLinkedList(object):

    def __init__(self):
        self.last = None

    def display_list(self):  # Traversing the linked list
        if self.last is None:
            print("List is empty")
            return

        p = self.last.link

        while True:
            print(p.info, end=" ")
            p = p.link
            if p == self.last.link:
                break

        print()

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp

    def insert_in_empty_list(self, data):
        temp = Node(data)
        self.last = temp
        self.last.link = self.last

    def insert_at_end(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp

    def insert_after(self, data, x):
        p = self.last.link

        while True:
            if p.info == x:
                break
            p = p.link
            if p == self.last.link:
                break
        if p == self.last.link and p.info != x:
            print(x, " not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
            if p == self.last:
                self.last = temp

    def delete_first_node(self):
        if self.last is None:  # List is empty
            return
        if self.last.link == self.last:   # List has only one node
            self.last = None
            return
        self.last.link = self.last.link.link

    def delete_last_node(self):
        if self.last is None:
            return # List is empty
        if self.last.link == self.last:  # List has only one node
            self.last = None
            return

        p = self.last.link
        while p.link is not self.last:
            p = p.link
        p.link = self.last.link
        self.last = p

    def delete_node(self, x):
        if self.last is None:  # List is empty
            return
        if self.last.link == self.last and self.last.info == x:  # Delete of only node
            self.last = None
            return

        if self.last.link.info == x:   # Delete first node
            self.last = None
            return

        p = self.last.link
        while p.link is not self.last.link:
            if p.link.info == x:
                break
            p = p.link

        if p.link == p.link.link:
            print(x, " not found in the list")
        else:
            p.link = p.link.link
            if self.last.info == x:
                self.last = p

    def create_list(self):
        n = int(input("Enter the number of Nodes: "))
        if n == 0:
            return

        data = int(input("Enter the element to be inserted: "))
        self.insert_in_empty_list(data)

        for i in range(n - 1):
            data = int(input("Enter the element to be inserted: "))
            self.insert_at_end(data)

    def concatenate(self, list2):
        if self.last is None:
            self.last = list2.last
            return

        if list2.last is None:
            return

        p = self.last.link
        self.last.link = list2.last.link
        list2.last.link = p
        self.last = list2.last


list1 = CircularLinkedList()
list1.creat_list()

while True:
    print("1.Display List ")
    print("2.Insert in empty list ")
    print("3.Insert a node in the beginning of the list")
    print("4.Insert a node at the end of the list")
    print("5.Insert a node after a specified node")
    print("6.Delete first node")
    print("7.Delete last node")
    print("8.Delete any node")
    print("9.Quit")

    option = int(input("Enter your choice"))

    if option == 1:
        list1.display_list()
    elif option == 2:
        data1 = int(input("Enter the element to be inserted: "))
        list1.insert_in_empty_list(data1)
    elif option == 3:
        data1 = int(input("Enter the element to be inserted: "))
        list1.insert_in_beginning(data1)
    elif option == 4:
        data1 = int(input("Enter the element to be inserted: "))
        list1.insert_at_end(data1)
    elif option == 5:
        data1 = int(input("Enter the element to be inserted: "))
        x = int(input("Enter the element after which to insert: "))
        list1.insert_at_end(data1)
    elif option == 6:
        list1.delete_first_node()
    elif option == 7:
        list1.delete_last_node()
    elif option == 8:
        data1 = int(input("Enter the element to be deleted: "))
        list1.delete_node(data1)
    elif option == 9:
        break
    else:
        print("Wrong option")
    print()




