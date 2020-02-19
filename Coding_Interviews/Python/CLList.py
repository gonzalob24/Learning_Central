class EmptyQueue(Exception):
    pass


class Node:

    def __init__(self, info, next):
        self.info = info
        self.next = next


class CLL:

    def __init__(self):
        self.header = Node("Start", None)
        self.header.next = self.header
        self.last = None  # Maintain a reference to the last node
        self.size = 0

    def is_empty(self):
        return self.header.next == self.header

    def display_cll(self):
        # if self.last is None:
        #     print("List is empty")
        #     return
        p = self.header.next

        while p.next != self.header.next:
            print(p.info, end=" ")
            p = p.next
            # if p == self.last.next:
            #     break
        print()

    def insert_at_front(self, value):
        if self.is_empty():
            temp = Node(value, None)
            self.header.next = temp
            self.last = temp
            self.last.next = self.header
            return
        self.header.next = Node(value, self.header.next)

    def insert_at_end(self, value):
        temp = Node(value, None)
        temp.next = self.header
        self.last.next = temp
        self.last = temp


if __name__ == "__main__":
    list1 = CLL()
    print(list1.is_empty())
    list1.insert_at_front(2)
    list1.insert_at_front(3)
    list1.insert_at_front(5)
    list1.insert_at_front(9)
    list1.display_cll()
    list1.insert_at_end(17)
    list1.display_cll()
    print(list1.last.info)
