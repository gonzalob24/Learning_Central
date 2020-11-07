# Class Node with different methods for the class SingleLinkedList
# I will be adding to the list and updating with comments later


class Node:

    def __init__(self, value):  # Constructor
        self.info = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # check if empty
    def isEmpty(self):
        return self.length == 0
    
    # Push new data
    def push(self, data):
        tempNode = Node(data)
        if(self.isEmpty()):
            self.head = tempNode
            self.tail = tempNode
        else:
            self.tail.next = tempNode
            self.tail = tempNode
        self.length+=1
    
    def pop(self):
        if(self.isEmpty()):
            return "List is empty"
        elif self.length == 1:
            p = self.head
            poppedItem = p.info
            self.head = None
            self.tail = None
        else:
            p = self.head
            while p.next.next is not None:
                p = p.next
            # remove the last node
            poppedItem = p.next.info
            self.tail = p
            p.next = None
        self.length-=1
        return poppedItem
            
    def display(self):
        if(self.isEmpty()):
            return "List is empty"
        else:
            p = self.head
            while p is not None:
                print(p.info, end='-->')
                p = p.next
        print('\n')

    def unshift(self, data):
        "Add front"
        tempNode = Node(data)
        if(self.isEmpty()):
            self.head = tempNode
            self.tail = tempNode
        else:
            tempNode.next = self.head
            self.head = tempNode
        self.length+=1

    def shift(self):
        "Remove front"
        if(self.isEmpty()):
            return 'List is empty'
        elif(self.length == 1):
            removedItem = self.head.info
            self.head = None
            self.tail = None
        else:
            removedItem = self.head.info
            self.head = self.head.next
        self.length-=1

        return removedItem

    def itemAt(self, data):
        if(data < 0 or data > self.length):
            return None
        else:
            p = self.head
            for i in range(data):
                p = p.next
            return p

    def set(self, data, index):
        foundNode = self.itemAt(index)
        if(not foundNode):
            return False
        else:
            foundNode.info = data
            return True

    def insert(self, data, index):
        foundNode = self.itemAt(index - 1)
        if(not foundNode):
            return False
        else:
            tempNode = Node(data)
            tempNode.next = foundNode.next
            foundNode.next = tempNode
            
            return True

    def getSize(self):
        return self.length

    def getLastItem(self):
        return self.tail.info


sll = SinglyLinkedList()
print(sll.isEmpty())
print(sll.display())
sll.push(10)
sll.push(9)
sll.push(8)
sll.push(4)
print(sll.getSize())
sll.display()
print('Removed:', sll.pop())
print('Removed:', sll.pop())
print('Removed:', sll.pop())
sll.display()
print('Removed:', sll.pop())
print(sll.display())
print(f'Size {sll.getSize()}')
sll.unshift(13)
sll.unshift(77)
print('Shift')
sll.push(9)
sll.push(4)
sll.display()
print(sll.itemAt(2))
print(sll.set(55, 2))
sll.display()
sll.insert(70, 2)
sll.display()





















# class SingleLinkedList:
#     def __init__(self):
#         self.start = None  # Initialize the start to None, first node of the list

#     def display_list(self):
#         if self.start is None:
#             print("List is empty")
#             # return ot needed
#         else:
#             print("List is: ")
#             p = self.start
#             while p is not None:
#                 print(p.info, " ", end='')
#                 p = p.link
#             print()

#     def count_nodes(self):
#         p = self.start
#         n = 0
#         while p is not None:
#             n += 1
#             p = p.link
#         print("Number of nodes in the list = ", n)

#     def search(self, x):
#         position = 1    # initialize position at 1
#         p = self.start  # start my reference to the first node
#         while p is not None:
#             if p.info == x:
#                 print(x, " is at position ", position)
#                 break
#             position += 1
#             p = p.link

#     # Reference to a predecessor of a node w/ particular info
#     def predecessor_of_node(self, x):
#         p = self.start
#         position = 1
#         while p is not None:
#             if p.link.info == x:
#                 print(p.info, " is at position, ", position)
#                 break
#             position += 1
#             p = p.link

#     def reference_node_at_position_k(self, k):
#         p = self.start
#         i = 1  # initial position
#         while i < k and p is not None:  # k is the position of the node we want to print
#             p = p.link
#             i += 1
#         print(p.info, " is located at position ", k)

#     def insert_in_beginning(self, data):
#         temp = Node(data)   # Creating a new Node
#         temp.link = self.start  # I want to link my node to the beginning of the list
#         self.start = temp

#     def insert_at_end(self, data):
#         temp = Node(data)
#         if self.start is None:      # Only if the list is empty
#             self.start = temp
#             return

#         p = self.start
#         while p.link is not None:   # making sure that our link is not empty
#             p = p.link
#         p.link = temp

#     def insert_after(self, data, x):  # Data is the value we want to insert
#         p = self.start
#         while p is not None:
#             if p.info == x:
#                 break
#             p = p.link

#         if p is None:
#             print(x, " not present in the list")
#         else:
#             temp = Node(data)
#             temp.link = p.link
#             p.link = temp

#     def insert_before(self, data, x):       # Data is the value we want to insert
#         # If list is empty
#         if self.start is None:
#             print("List is empty")
#             return

#         # x is in first node, new node is to be inserted before first node
#         if x == self.start.info:
#             temp = Node(data)
#             temp.link = self.start
#             self.start = temp
#             return

#         # Find references to predecessor of node containing x
#         p = self.start
#         while p.link is not None:
#             if p.link.info == x:
#                 break
#             p = p.link

#         if p.link is None:
#             print(x, " not present in the list")
#         else:
#             temp = Node(data)
#             temp.link = p.link
#             p.link = temp

#     def insert_at_position(self, data, k):   # Insert a node at a given position
#         if k == 1:
#             temp = Node(data)
#             temp.link = self.start
#             self.start = temp
#             return

#         p = self.start
#         i = 1
#         while i < k - 1 and p is not None:  # Reference to k - 1
#             p = p.link
#             i += 1

#         if p is None:
#             print('You can only insert up to position ', i)
#         else:
#             temp = Node(data)
#             temp.link = p.link
#             p.link = temp

#     def delete_first_node(self):
#         if self.start is None:
#             return
#         self.start = self.start.link

#     def delete_last_node(self):
#         if self.start is None:
#             return

#         if self.start.link is None:
#             self.start = None
#             return

#         p = self.start
#         while p.link.link is not None:
#             p = p.link
#         p.link = None

#     def delete_node(self, x):
#         if self.start is None:
#             print("List is empty")
#             return

#         # Deletion of first node
#         if self.start.info == x:
#             self.start = self.start.link
#             return

#         # Deletion in between or at the end
#         p = self.start
#         while p.link is not None:
#             if p.link.info == x:
#                 break
#             p = p.link

#         if p.link is None:
#             print('Element ', x, ' nor in list')
#         else:
#             p.link = p.link.link

#     def reverse_list(self):
#         prev = None     # Initialize prev to None
#         p = self.start
#         while p is not None:
#             next1 = p.link
#             p.link = prev
#             prev = p
#             p = next1
#         self.start = prev

#     def create_list(self):
#         n = int(input("Enter the number of nodes: "))
#         if n == 0:
#             return
#         for i in range(n):
#             data = int(input("Enter the element to be inserted: "))
#             self.insert_at_end(data)

#     def bubble_sort_exchange_data(self):
#         end = None
#         # Stop end when end refers to second Node
#         # or when p.link == end
#         while end != self.start.link:
#             p = self.start
#             while p.link != end:
#                 q = p.link
#                 if p.info > q.info:
#                     p.info, q.info = q.info, p.info
#                 p = p.link
#             end = p

#     def bubble_sort_linked_list_exchange_links(self):
#         end = None

#         while end != self.start.link:
#             r = p = self.start
#             while p.link != end:
#                 q = p.link
#                 if p.info > q.info:
#                     p.link = q.link
#                     q.link = p
#                     if p != self.start:
#                         r.link = q
#                     else:
#                         self.start = q
#                     p, q = q, p
#                 r = p
#                 p = p.link
#             end = p

#     def merge_sort(self):
#         self.start = self._merge_sort_rec(self.start)

#     def _merge_sort_rec(self, list_start):
#         # If list is empty or has one element
#         if list_start is None or list_start.link is None:
#             return list_start

#         # If more than one element
#         start1 = list_start
#         start2 = self._divide_list(list_start)
#         start1 = self._merge_sort_rec(start1)
#         start2 = self._merge_sort_rec(start2)
#         startM = self._merge2(start1, start2)
#         return startM

#     def _divide_list(self, p):
#         q = p.link.link
#         while q is not None and q.link is not None:
#             p = p.link
#             q = q.link.link
#         start2 = p.link
#         p.link = None
#         return start2

#     def has_cycle(self):
#         if self.find_cycle() is None:
#             return False
#         else:
#             return True

#     def find_cycle(self):
#         if self.start is None or self.start.link is None:
#             return None

#         slowR = self.start
#         fastR = self.start

#         while fastR is not None and fastR.link is not None:
#             slowR = slowR.link
#             fastR = fastR.link.link
#             if slowR == fastR:
#                 return slowR  # Returns the reference or the node where the two Nodes meet
#         return None

#     def remove_cycle(self):
#         c = self.find_cycle()  # first find if there is a cycle, this references to that node
#         if c is None:
#             return

#         print("Node at which the cycle was detected is ", c.info)
#         # To find the length of lift first we need to find the length of the cycle
#         p = c
#         q = c
#         len_cycle = 0

#         while True:
#             len_cycle += 1
#             q = q.link
#             if p == q:
#                 break

#         print("Length of cycle is ", len_cycle)

#         len_rem_list = 0
#         p = self.start
#         while p != q:
#             len_rem_list += 1
#             p = p.link
#             q = q.link

#         print("Number of Nodes not included in the cycle area : ", len_rem_list)
#         length_list = len_cycle + len_rem_list
#         print("Length of the list is : ", length_list)

#         # Removing the cycle from the list
#         p = self.start
#         for i in range(length_list - 1):
#             p = p.link
#         p.link = None

#     def insert_cycle(self, x):
#         if self.start is None:
#             return
#         p = self.start
#         px = None
#         prev = None

#         while p is not None:
#             if p.info == x:
#                 px = p
#             prev = p
#             p = p.link

#         if px is not None:
#             prev.link = px
#         else:
#             print(x, " not present in list")

#     def concatenate(self, list2):
#         if self.start is None:
#             self.start = list2.start
#             return

#         if list2.start is not None:
#             return

#         p = self.start
#         while p.link is not None:
#             p = p.linl

#         p.link = list2.start


# list1 = SingleLinkedList()
# list1.display_list()
# list1.insert_at_end(1)
# list1.insert_at_end(10)
# list1.display_list()
# list1.create_list()

"""
while True:
    print("1.Display List")
    print("2.  Count the number of nodes")
    print("3.  Search for an element")
    print("4.  Insert an empty list/Insert in the beginning of the list")
    print("5.  Insert a node at the end of the list")
    print("6.  Insert a node after a specified node")
    print("7.  Insert a node before a specified node")
    print("8.  Inset a node at a given position")
    print("9.  Delete first node")
    print("10. Delete last node")
    print("11. Delete any node")
    print("12. Reverse the list")
    print("13. Bubble sort by exchanging data")
    print("14. Bubble sort by exchanging links")
    print("15. MergeSort")
    print("16. Insert Cycle")
    print("17. Detect Cycle")
    print("18. Remove Cycle")
    print("19. Quit")


option = int(input("Enter your choice: "))
"""

# list1.display_list()
# print("search")
# list1.search(5)
# print("Predecessor of node with particular info")
# list1.predecessor_of_node(5)
# list1.reference_node_at_position_k(3)
# list1.bubble_sort_exchange_data()
# list1.display_list()
