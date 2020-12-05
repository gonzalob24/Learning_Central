# This is an easy way to implement a queue however it is not the best way
# because it takes long O(NlogN) becuse I am sorting every time I am inserting
# an element to the PQ
class PriorityQueue():
    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):
        self.values.append({"value": value, "priority": priority})
        self.values = sorted(self.values, key=lambda node: node["priority"])

    def dequeue(self):
        return self.values.pop(0)

    def display(self):
        # for obj in self.values:
        # print(f'{obj["value"]}:{obj["priority"]}').
        index = 0
        while index < len(self.values):
            vertex = self.values[index]
            print(f'{vertex["value"]}:{vertex["priority"]}')
            index += 1


# q = PriorityQueue()
# q.enqueue("B", 3)
# q.enqueue("C", 5)
# q.enqueue("D", 2)
# q.enqueue("Q", 20)
# q.enqueue("P", 1.5)
# q.display()
# print(q.dequeue())
# q.display()
