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

    def dequeue(self):
        # first swap root and last element
        self.pqArr[0], self.pqArr[self.current_index] = self.pqArr[self.current_index], self.pqArr[0]
        # place this element in the correct location
        element_to_restore = self.pqArr[0]
        removedNode = self.pqArr.pop()
        pqArr_length = len(self.pqArr)
        self.current_index -= 1
        # get the parent index starting from root
        parentIndex = 0

        while True:
            # get both left and right child index
            lchildIndex = parentIndex * 2 + 1
            rchildIndex = parentIndex * 2 + 2
            # store child nodes in variables and keep track of the index where swapp occurs
            leftChild = None
            rightChild = None
            swap = None

            if lchildIndex < pqArr_length:
                # store left child in variable
                leftChild = self.pqArr[lchildIndex]
                # compare priorities
                if leftChild.priority < element_to_restore.priority:
                    swap = lchildIndex

            if rchildIndex < pqArr_length:
                rightChild = self.pqArr[rchildIndex]
                if swap == None and rightChild.priority < element_to_restore.priority or \
                        swap != None and rightChild.priority < leftChild.priority:
                    swap = rchildIndex
            # if I did not swap break
            if swap == None:
                break

            self.pqArr[parentIndex], self.pqArr[swap] = self.pqArr[swap], self.pqArr[parentIndex]

            # updare parentIndex
            parentIndex = swap
        return f'removedNode: {removedNode.info}: {removedNode.priority}'

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
    print('Deleted Node')
    print(pq1.dequeue())
    pq1.display_pq_array()
