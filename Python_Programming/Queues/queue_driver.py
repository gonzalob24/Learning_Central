class Queue:
    def __init__(self):
        self.queue_list = []
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]

    def back(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def size(self):
        return self.length

    def enqueue(self, data):
        self.queue_list.append(data)
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        front = self.front()
        self.queue_list.remove(front)
        self.length -= 1
        return front

    def print_queue(self):
        for item in self.queue_list:
            print(f'{item}', end='-->')
        print('end')


q = Queue()
print(q.is_empty())
print(q.front())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print_queue()
print(q.dequeue())
q.print_queue()
