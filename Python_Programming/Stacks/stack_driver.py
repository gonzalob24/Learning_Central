class Stack:
    def __init__(self):
        self.stack_list = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def top(self):
        if self.is_empty():
            return None

        return self.stack_list[self.length - 1]

    def size(self):
        return self.length

    def push(self, data):
        self.stack_list.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()
