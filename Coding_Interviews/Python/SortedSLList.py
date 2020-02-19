class Node:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next


class SortedSLList:

    def __init__(self):
        self.header = Node("start")
        self.size = 0

    def add_value(self, value):
        temp = Node(value)
        if self.header.next is None:
            self.header.next = temp
            self.size += 1
            return

        p = self.header
        while p.next is not None and p.next.info < temp.info:
            p = p.next

        temp.next = p.next
        p.next = temp

    def display_list(self):
        p = self.header
        while p.next is not None:
            p = p.next
            print(p.info, end=" ")
        print()


if __name__ == "__main__":
    list1 = SortedSLList()
    list1.add_value(10)
    list1.add_value(2)
    list1.add_value(3)
    list1.add_value(5)
    list1.add_value(8)
    list1.add_value(12)
    list1.add_value(6)
    list1.add_value(7)
    list1.add_value(11)
    list1.add_value(6)
    list1.add_value(1)
    list1.display_list()
