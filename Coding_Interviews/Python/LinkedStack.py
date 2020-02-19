class Node:
    """
    Creates a node to be used when pushing elements to the stack
    next is None by default
    """
    def __init__(self, info, next=None):
        self.info = info
        self.next = next



class LinkedStack:
    """
    The top of the stack will be the front of my Linked list
    """
    def __init__(self):
        self.header = Node("start")
        self.size = 0

    def push(self, value):
        """
        push values to the top of the stack.
        """
        self.header.next = Node(value, self.header.next)
        self.size += 1

    def pop(self):
        popped_item = self.header.next.info
        self.header.next = self.header.next.next
        self.size -= 1
        return popped_item

    def display(self):
        print("[", end="")
        p = self.header.next
        while p is not None:
            print(p.info, end=" ")
            p = p.next
        print("]")


if __name__ == "__main__":
    stack1 = LinkedStack()
    stack1.push(1)
    stack1.push(2)
    stack1.push(43)
    stack1.display()
    print(stack1.pop())
    stack1.display()
