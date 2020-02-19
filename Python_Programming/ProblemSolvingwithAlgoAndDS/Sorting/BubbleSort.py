from Node1 import Node


class BubbleSort:
    def __init__(self):
        self.start = None

    def bubble_sort_exchange_data(self):
        end = None

        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubble_sort_linked_list_exchange_links(self):
        end = None

        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    p, q = q, p
                r = p
                p = p.link
            end = p


def bubble_sort(list_of_nums):
    for x in range(len(list_of_nums) - 1, 0, - 1):   # From length of list - 1, to 0, decrement by 1
        swaps = 0
        for j in range(x):
            if list_of_nums[j] > list_of_nums[j + 1]:
                list_of_nums[j], list_of_nums[j + 1] = list_of_nums[j + 1], list_of_nums[j]
                swaps += 1
        if swaps == 0:
            break
