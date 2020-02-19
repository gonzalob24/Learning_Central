class Node(object):

    def __init__(self, value):
        self.info = value
        self.link = None


class HeaderLinkedList(object):

    def __init__(self):
        self.head = Node(0)

    def display_list(self):
        if self.head.link is None:
            print("List is empty")
            return

        p = self.head.link
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

    def insert_at_end(self, data):
        temp = Node(data)

        p = self.head
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
            i+=1

        if p is None:
            print("You can insert only upto ", (i - 1), "th position")
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
            next = p.link
            p.link = prev
            prev = p
            p = next

        self.head.link = prev


list_test = HeaderLinkedList()
list_test.create_list()
