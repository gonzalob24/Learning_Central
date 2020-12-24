# playing around with first linked lists

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


def print_list(node10):
    while node10 is not None:
        print(node10, end=" ")
        node10 = node10.next
    print()


def print_backwards(list2):
    if list2 is None:
        return
    head = list2
    tail = list2.next
    print_backwards(tail)
    print(head, end=" ")


def remove_node(list1):
    if list1 is None:
        return
    first = list1
    second = list1.next
    # Make the first node refer to to the second
    first.next = second.next
    # Separate the second node from the rest of the list
    second.next = None
    return second


def print_backwards_nicelt(list3):
    print("[", end=" ")
    print_backwards(list3)
    print("] ")


node = Node("test")
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
print(node)
node1.next = node2
node2.next = node3
print(node2)
print("While test with node1")

print_list(node1)
print_backwards(node1)
print()
print_backwards_nicelt(node1)
removed = remove_node(node1)
print(removed)
print_list(node1)

