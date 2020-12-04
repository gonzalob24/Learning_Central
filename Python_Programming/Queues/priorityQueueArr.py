import math

# Set up a node


class Node:
    def __init__(self, value, priority):
        self.info = value
        self.priority = priority


class PQArray:
    def __init__(self):
        self.pqArr = []
        self.current_index = -1

    # {1:priority}-{2:priority}-{3:priority}

    def isEmpty(self):
        return len(self.pqArr) == 0

    # O(log n)
    def enqueue(self, data, priority):
        # create new node
        newNode = Node(data, priority)

        if self.isEmpty():
            self.pqArr.append(newNode)  # append the new node
        else:
            self.pqArr.append(newNode)
            index = self.current_index
            insertedValue = self.pqArr[index]

            while index > 0:
                parentIndex = math.floor((index - 1) / 2)
                if insertedValue.priority >= self.pqArr[parentIndex].priority:
                    break
                self.pqArr[index], self.pqArr[parentIndex] = self.pqArr[parentIndex], self.pqArr[index]

                index = parentIndex
        self.current_index += 1

    def dequeue():
        pass

    def display_pq_array(self):
        count = 0
        while count <= self.current_index:
            currentNode = self.pqArr[count]
            print(currentNode.info, currentNode.priority)
            count += 1


if __name__ == "__main__":
    pq1 = PQArray()
    print(pq1.isEmpty())
    pq1.enqueue("Gold", 5)
    pq1.enqueue("Gun shot", 1)
    pq1.enqueue("Fever", 4)
    pq1.enqueue("Broken Arm", 2)
    pq1.enqueue("Nail in foot", 3)
    pq1.display_pq_array()
