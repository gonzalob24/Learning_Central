class Node:

    def __init__(self, value):
        self.info = value
        self.link = None


class HeaderLinkedList:

    def __init__(self):
        self.head = Node(0)  # Constructor refers to the header node, it could be empty

    def display_list(self):
        if self.head.link is None:
            print("List is empty")
            return

        p = self.head.link  # Which is a reference to the second node
        print("List is: ")
        while p is not None:
            print(p.info, end=" ")
            p = p.link
        print()

    def create_list(self):
        n = int(input("Enter the number of nodes: "))

        for i in range(n):
            data = int(input("Enter the element to be inserted: "))
            self.insert_at_end(data)
        print()

    def insert_at_end(self, data):
        temp = Node(data)  # Node created with specific value

        p = self.head  # Header Node
        while p.link is not None:
            p = p.link
        p.link = temp

    def insert_before(self, data, x):
        # Find reference to predecessor of node containing x
        p = self.head
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print(x, " not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, k):
        p = self.head
        i = 1
        while i <= k - 1 and p is not None:
            p = p.link
            i += 1

        if p is None:
            print("You can insert only up to ", (i - 1), "th position")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, data):
        p = self.head
        while p.link is not None:
            if p.link.info == data:
                break
            p = p.link

        if p.link is None:
            print(data, " not found")
        else:
            p.link = p.link.link

    def reverse_list(self):
        prev = None
        p = self.head.link
        while p is not None:
            nextt = p.link
            p.link = prev
            prev = p
            p = nextt

        self.head.link = prev


list_test = HeaderLinkedList()
list_test.create_list()

while True:
    print("1.Display List ")
    print("2.Insert a node at the end of the list")
    print("3.Insert a node before a specified node")
    print("4.Insert a node at a given position")
    print("5.Delete a node")
    print("6.Reverse the list")
    print("7.Quit")

    option = int(input("Enter your choice"))

    if option == 1:
        list_test.display_list()
    elif option == 2:
        data1 = int(input("Enter the element to be inserted: "))
        list_test.insert_at_end(data1)
    elif option == 3:
        data1 = int(input("Enter the element to be inserted: "))
        where = int(input("Enter the element before insertion: "))
        list_test.insert_before(data1, where)
    elif option == 4:
        data1 = int(input("Enter the element to be inserted: "))
        position = int(input("Enter the position number to insert element: "))
        list_test.insert_at_position(data1, position)
    elif option == 5:
        data1 = int(input("Enter the element to be deleted: "))
        list_test.delete_node(data1)
    elif option == 6:
        list_test.reverse_list()
    elif option == 7:
        break
    else:
        print("Wrong option")

    print()

