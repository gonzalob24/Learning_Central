from node import Node
from SingleLinkedList import SingleLinkedList


def insert_at_head(lst, value):
    temp_node = Node(value)
    if lst.head_node is None:
        lst.head_node = temp_node
        return
    temp_node.next_element = lst.head_node
    lst.head_node = temp_node


def insert_at_tail(lst, value):
    temp_node = Node(value)
    if lst.head_node is None:
        lst.head_node = temp_node
        return
    p = lst.head_node
    while p.next_element is not None:
        p = p.next_element
    p.next_element = temp_node
    return


def search(lst, value):
    if lst.head_node is None:
        return "Value not found, List is empty"

    p = lst.head_node

    while p is not None:
        if p.data == value:
            return p
        p = p.next_element

    return False


def recursive_search(node, value):
    if node is None:
        return False

    if node.data == value:
        return True

    return recursive_search(node.next_element, value)


def delete_at_head(lst):
    if lst.is_empty():
        return "List is empty"

    lst.head_node = lst.head_node.next_element


def delete_value(lst, value):
    deleted = False
    if lst.is_empty():
        return "List is empty"

    # delete_node = search(lst, value)
    if lst.head_node.data == value:
        lst.delete_at_head()
        deleted = True
        return deleted
    p = lst.head_node
    prev = None
    while p is not None:
        if p.data == value:
            prev.next_element = prev.next_element.next_element
            deleted = True
            break
        prev = p
        p = p.next_element

    return deleted


def length(lst):
    if lst.is_empty():
        return 0
    p = lst.get_head()
    length = 0
    while p is not None:
        p = p.next_element
        length += 1
    return length


def reverse(lst):
    if lst.is_empty() or length(lst) == 1 or lst is None:
        return lst

    prev = None
    current = lst.get_head()
    future = current.next_element

    while current is not None:
        future = current.next_element
        current.next_element = prev

        prev = current
        current = future
    lst.head_node = prev
    return lst


def detect_loop(lst):
    slow = lst.get_head()
    fast = lst.get_head()

    while fast is not None and fast.next_element is not None:
        slow = slow.next_element
        fast = fast.next_element.next_element
        if slow == fast:
            return True

    return False


def remove_duplicates(lst):
    memo = {}

    if lst.is_empty():
        return lst

    p = lst.get_head()
    unique_list = SingleLinkedList()
    while p is not None:
        if p.data not in memo:
            memo[p.data] = p.data
            insert_at_tail(unique_list, p.data)

        p = p.next_element
    return unique_list


l = SingleLinkedList()
# l.insert_at_head(1)
# l.insert_at_head(2)
# l.insert_at_head(3)
# l.insert_at_head(4)
# l.insert_at_head(5)
# l.print_list()
insert_at_tail(l, 1)
insert_at_tail(l, 2)
insert_at_tail(l, 2)
insert_at_tail(l, 3)
insert_at_tail(l, 4)
insert_at_tail(l, 4)
# l.print_list()
# print(search(l, 4))  # returns a node
# print(recursive_search(l.head_node, 3))
# delete_at_head(l)
# delete_at_head(l)
# delete_value(l, 44)
# reverse(l)
l = remove_duplicates(l)
l.print_list()
