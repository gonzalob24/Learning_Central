class Node:

    def __init__(self, value):
        self.info = value
        self.next = None

    def get_data(self):
        return self.info

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.info = new_data

    def set_next(self, new_next):
        self.next = new_next
