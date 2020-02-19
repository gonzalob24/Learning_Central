class Node:

    def __init__(self, info, priority, next=None):
        self.info = info
        self.next = next
        self.priority = priority


class PriorityQueue:
    """
    add_item()
    delete_highest_priority()
    size()
    """

    def __init__(self):
        self.header = Node("Empty", -1, None)
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add_item(self, value, priority):
        p = self.header
        temp = Node(value, priority)

        if self.is_empty() or priority >= p.next.priority:
            self.header.next = Node(value, priority, self.header.next)
            self.size += 1
        else:
            while p.next is not None and p.next.priority > priority:
                p = p.next
            if p.next is None:
                p.next = temp
                self.tail = temp
            else:
                temp.next = p.next
                p.next = temp
            self.size += 1

    def display(self):
        p = self.header.next

        while p is not None:
            print("Info: ", p.info, "\tPriority:\t", p.priority)
            p = p.next

    def queue_size(self):
        return self.size

    def delete_highest_priority(self):
        highest_priority = self.header.next
        self.header = self.header.next
        self.size -= 1
        print("\nDeleted:\n", "Info: ", highest_priority.info, "\tPriority:\t", highest_priority.priority, sep="")

    def show_lowest_priority(self):
        return self.tail

    def print(self, node):
        return "\nLowest Priority:\nInfo: " + str(node.info) + "\tPriority:\t" + str(node.priority)

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.add_item(10, 15)
    pq.add_item(9, 1)
    pq.add_item(1, 4)
    pq.add_item(18, 17)
    pq.add_item(11, 20)
    pq.display()
    print(pq.queue_size())
    pq.delete_highest_priority()

    print(pq.print(pq.show_lowest_priority()))
    print()
    pq.display()
