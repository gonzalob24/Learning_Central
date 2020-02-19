class Stack:
    def __inir__(self):
        self.item = []  # empty list

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

