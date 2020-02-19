class Node:

    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("Lis is : ")
            p = self.start
            while p is not None:
                print(p.info, end='')
                p = p.link
            print()

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def merge1(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge1(self.start, list2.start)
        return merge_list

    # Merging two linked lists p1 and p2 assuming they are sorted
    def _merge1(self, p1, p2):
        if p1.info <= p2.info:
            startM = Node(p1.info)
            p1 = p1.link
        else:
            startM = Node(p2.info)
            p2 = p2.link

        pM = startM  # Refers to the newly inserted Node of merged list

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = Node(p1.info)
                p1 = p1.link
            else:
                pM.link = Node(p2.info)
                p2 = p2.link
            pM = pM.link

        # If second list has finished and elements left in first list
        while p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link
            pM = pM.link

        # If first list had finished and elements left in second list
        while p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            pM = pM.link

        return startM

    # by rearranging links we don't allocate info to new Linked List
    def merge2(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge2(self.start, list2.start)
        return merge_list

    def _merge2(self, p1, p2):

        if p1.info <= p2.info:
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link

        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = p1
                pM = pM.link
                p1 = p1.link
            else:
                pM.link = p2
                pM = pM.link
                p2 = p2.link

        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1

        return startM

    def merge_sort(self):
        self.start = self._merge_sort_rec(self.start)

    def _merge_sort_rec(self, list_start):
        # If list is empty or has one element
        if list_start is None or list_start.link is None:
            return list_start

        # If more than one element
        start1 = list_start
        start2 = self._divide_list(list_start)
        start1 = self._merge_sort_rec(start1)
        start2 = self._merge_sort_rec(start2)
        startM = self._merge2(start1, start2)
        return startM

    def _divide_list(self, p):
        q = p.link.link
        while q is not None and q.link is not None:
            p = p.link
            q = q.link.link
        start2 = p.link
        p.link = None
        return start2

    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True

    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None

        slowR = self.start
        fastR = self.start

        while fastR is not None and fastR.link is not None:
            slowR = slowR.link
            fastR = fastR.link.link
            if slowR == fastR:
                return slowR
        return None

    def remove_cycle(self):
        c = self.find_cycle()
        if c is None:
            return
        print("Node at which the cycle was detected is ", c.info)

        p = c
        q = c
        len_cycle = 0

        while True:
            len_cycle += 1
            q = q.link
            if p == q:
                break

        print("Length of cycle is ", len_cycle)

        len_rem_list = 0
        p = self.start
        while p != q:
            len_rem_list += 1
            p = p.link
            q = q.link

        print("Number of Nodes not included in the cycle area : ", len_rem_list)
        length_list = len_cycle + len_rem_list
        print("Length of the list is : ", length_list)

        p = self.start
        for i in range(length_list - 1):
            p = p.link
        p.link = None

    def insert_cycle(self, x):
        if self.start is None:
            return
        p = self.start
        px = None
        prev = None

        while p is not None:
            if p.info == x:
                px = p
            prev = p
            p = p.link

        if px is not None:
            prev.link = px
        else:
            print(x, " not present in list")
