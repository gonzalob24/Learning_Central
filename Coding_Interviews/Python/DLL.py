class Node:

    def __init__(self, info, prev, next):
        self.info = info
        self.next = next
        self.prev = prev


class DLL:

    def __init__(self):
        self.header = Node("Start", None, None)
        self.header.next = self.header
        self.header.prev = self.header

    def display(self):
        # if self.header.next is None:
        #     print("My DLL is empty")
        # else:
        #     # p is a reference to the first node
        #     p = self.header.next
        #     while p is not None:
        #         print(p.info, end=" ")
        #         p = p.next

        p = self.header.next
        while p != self.header:
            print(p.info, end=" ")
            p = p.next
        print()

    def add_front(self, value):
        # self.header.next = Node(value, self.header, self.header.next)
        # temp = Node(value, None, None)
        # if self.header.next is None:
        #     self.header.next = temp
        #     temp.prev = self.header
        # else:
        #     temp.next = self.header.next
        #     self.header.next = temp
        #     self.header.next.prev = temp

        # working below
        # temp = Node(value, None, self.header.next)
        # self.header.next = temp
        # self.header.next.prev = self.header.next

        temp = Node(value, self.header, self.header.next)
        self.header.next.prev = temp
        self.header.next = temp

    def add_end(self, value):
        temp = Node(value, self.header.prev, self.header)
        self.header.prev.next = temp
        self.header.prev = temp


if __name__ == "__main__":

    dll1 = DLL()
    dll1.display()
    dll1.add_front("#")
    dll1.add_front(4)
    dll1.add_front(15)
    dll1.add_end(22)
    dll1.add_end(16)
    dll1.display()
