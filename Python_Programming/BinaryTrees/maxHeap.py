import math


class MaxHeap:
    def __init__(self):
        self.array = []
        self.current_Index = -1

    def isEmpty(self):
        return len(self.array) == 0

    def insert(self, data):
        if(self.isEmpty()):
            self.array.append(data)
        else:
            # append element then restore/heapify to correct location
            self.array.append(data)
            index = self.current_Index
            insertedValue = self.array[index]

            # do this until index > 0: sawp if parent is <= its child
            while index > 0:
                # get the parent
                parentIndex = math.floor((index - 1) / 2)
                # compare parent with children, break if insertedValue us <= parent
                # b/c the inserted value is in the correct location
                if (insertedValue <= self.array[parentIndex]):
                    break
                # Swap if insertedValue is > parentIndex value
                # Swap if insertedValue is > parentIndex value

                self.array[index], self.array[parentIndex] = self.array[parentIndex], self.array[index]

                # update index after swap
                index = parentIndex
        self.current_Index += 1

    def delete_max(self):
        # swap root with last item
        self.array[0], self.array[self.current_Index] = self.array[self.current_Index], self.array[0]

        # delete last element
        element = self.array[0]
        length_mh = len(self.array)
        # delete and store last element
        maxValue = self.array.pop()

        # start at root and heapify down / restore down
        parentIndex = 0

        # do this as long as while loop is true
        while True:
            l_childIndex = parentIndex * 2 + 1
            r_childIndex = parentIndex * 2 + 2
            leftChild = None
            rightChild = None
            swap = None

            if l_childIndex < length_mh:
                leftChild = self.array[l_childIndex]
                if leftChild > element:
                    swap = l_childIndex
            if r_childIndex < length_mh:
                rightChild = self.array[r_childIndex]
                if (swap == None and rightChild > element) or (swap != None and rightChild > leftChild):
                    swap = r_childIndex
            if swap == None:
                break

            self.array[parentIndex] = self.array[swap]
            self.array[swap] = element

        return maxValue

    def display_max_heap_array(self):
        return self.array


mh = MaxHeap()
mh.insert(100)
mh.insert(200)
mh.insert(20)
mh.insert(80)
mh.insert(99)

print(mh.display_max_heap_array())
print(mh.delete_max())
print(mh.display_max_heap_array())
