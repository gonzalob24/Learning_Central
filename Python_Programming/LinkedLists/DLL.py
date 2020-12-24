from node_DLL import Node


class DoublyLinkedList:
    def __init__(self):
        self.head__node = None
        self.tail_node = None

    def is_empty(self):
        return self.head__node is None

    def get_head(self):
        return self.head__node

    def insert_at_head(self, value):
        temp_node = Node(value)
        if self.is_empty():
            self.head__node = temp_node
            return

        temp_node.next_element = self.head__node
        self.head__node.previous_element = temp_node
        self.head__node = temp_node
        return

    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True
