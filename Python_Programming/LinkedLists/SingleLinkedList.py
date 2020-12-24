class SingleLinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        return self.head_node is None

    def print_list(self):
        p = self.head_node

        while p is not None:
            print(p.data, end="-->")
            p = p.next_element
        print("None")
