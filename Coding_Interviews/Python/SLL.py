class EmptyList(Exception):
    pass


class Node:

    def __init__(self, info, next):
        self.info = info
        self.next = next


class SLL:

    def __init__(self):
        self.header = Node("empty", None)
        self.tail = self.header
        self.size = 0

    def is_empty(self):
        return self.header.next is None

    def display(self):
        if self.is_empty():
            print("My SLL is empty.\n")
            return
        else:
            print("My list is: ", end="")
            p = self.header.next
            while p is not None:
                print(p.info, end=" ")
                p = p.next
        print("\n")

    def add_front(self, value):
        self.header.next = Node(value, self.header.next)
        self.size += 1

    def add_end(self, value):
        temp = Node(value, None)

        p = self.header
        while p.next is not None:
            p = p.next
        p.next = temp
        self.size += 1

    def delete(self, value):
        p = self.header
        if self.is_empty():
            raise EmptyList("My SLL is empty.")
        else:
            while p.next is not None and p.next.info != value:
                p = p.next
            if p.next is None:
                print("Reached end of the list {} was not found\n".format(value))
            else:
                deleted_value = p.next.info
                p.next = p.next.next
                return deleted_value
        self.size -= 1

    def delete_at_pos(self, position):
        p = self.header
        idx = 0

        while idx < position:
            p = p.next
            idx += 1
        deleted_item = p.next.info
        p.next = p.next.next
        print(deleted_item)
        self.size -= 1

    def delete_mth_to_last(self, mth):
        pcurrent = self.header
        pnext = self.header
        idx = 0
        if self.header.next is None:
            print("List is empty:")
            return
        elif mth >= self.size:
            print("List is not big enough")
            return
        else:
            while pnext.next is not None:
                pnext = pnext.next
                if idx > mth:
                    pcurrent = pcurrent.next
                idx += 1
            deleted_item = pcurrent.next.info
            pcurrent.next = pcurrent.next.next
            print(deleted_item)
            self.size -= 1

    def insert_after(self, value_in, after_x):
        if self.is_empty():
            raise EmptyList("My SLL is empty")
            return
        else:
            p = self.header
            while p.next is not None and p.info != after_x:
                p = p.next
            if p.info != after_x:
                print("Reached end of the list {} was not found\n".format(after_x))
            else:
                p.next = Node(value_in, p.next)
        self.size += 1

    def mth_to_last(self, mth):
        element_position = self.size - mth
        p = self.header.next
        if self.header.next is None:
            print("List is empty")
            return
        elif mth >= self.size:
            print("List is not big enough")
            return
        else:
            index = 1
            while index != element_position:
                p = p.next
                index += 1
            return p.info
            self.size -= 1

    def find_cylce(self):
        fastP = self.header.next
        slowP = self.header.next

        if self.header.next is None:
            print("List is empty")
            return
        while fastP is not None and fastP.next is not None:
            fastP = fastP.next.next
            slowP = slowP.next
            if slowP == fastP:
                # print("Cycle found")
                return slowP  # return the node where items are the same
        return False

    def has_a_cycle(self):
        if self.find_cylce() is None:
            return False
        else:
            return True

    def remove_cycle(self):
        """
        To remove the cycle we need to first find the length of the cycle
        """
        cycle_node = self.find_cylce()  # node where the cycle was first detected where slow and fast references meet
        if cycle_node is None:
            return
        print("Node where cycle was detected ", cycle_node.info)

        q = cycle_node  # will move q until it is equal to p to count the length of the cycle
        cycle_length = 0
        while True:
            cycle_length += 1
            q = q.next
            if q == cycle_node:
                break
        print("Length of the cycle is: ", cycle_length)

        # Count the number fo remaining nodes
        length_remaining = 0
        p = self.header.next  # move the position of p to the begning of the list
        while p != q:
            length_remaining += 1
            p = p.next
            q = q.next
        print("Number of nodes not in the cycle: ", length_remaining)

        list_length = cycle_length + length_remaining  # length of my list
        print("Length of the list is: ", list_length)

        # remove the cycle move p to the start of the list
        p = self.header
        for i in range(list_length - 1):
            p = p.next
        p.next = None

    def insert_cycle(self, cycle_position):
        if self.header.next is None:
            return
        p = self.header
        insert_cycle_here = None
        idx = 0
        while p.next is not None:
            p = p.next
            idx += 1
            if idx == cycle_position:
                insert_cycle_here = p

        p.next = insert_cycle_here


if __name__ == "__main__":
    # def find_cylce(SList):
    #     fastP = SList.header.next
    #     slowP = SList.header.next
    #
    #     if SList.header.next is None:
    #         print("List is empty")
    #         return
    #     while fastP is not None and fastP.next is not None:
    #         fastP = fastP.next.next
    #         slowP = slowP.next
    #         if slowP == fastP:
    #             print("Cycle found")
    #             return True
    #     return False

    sll1 = SLL()
    sll1.add_end(1)
    sll1.add_end(2)
    sll1.add_end(3)
    sll1.add_end(4)
    sll1.add_end(5)
    sll1.add_end(6)
    sll1.add_end(7)
    sll1.display()
    sll1.insert_cycle(5)
    print(sll1.has_a_cycle())
    sll1.remove_cycle()
    #sll1.delete_mth_to_last(0)
    #print(sll1.mth_to_last(2))
    #sll1.display()
    # sll1.delete(1)
    # sll1.display()
    # sll1.add_front(100)
    # sll1.add_front(3)
    # sll1.add_front(4)
    # sll1.display()
    # sll1.add_end(4)
    # sll1.display()
    # sll1.add_end(9)
    # sll1.add_end(12)
    # sll1.add_front(34)
    # sll1.display()
    # sll1.delete(90)
    # sll1.insert_after(10, 9)
    # sll1.insert_after(1, 34)
    # sll1.display()

