# Heap Tree array implementation
class HeapEmptyError(Exception):
    pass


class Heap:

    def __init__(self, maxSize=20):
        self.a = [None] * maxSize
        self.n = 0
        # all values in the heap should be less than this value
        self.a[0] = 99999

    def insert(self, value):
        self.n += 1  # increment the size of the heap
        self.a[self.n] = value
        self.restore_up(self.n)  # this places the key in its proper place

    def restore_up(self, i):  # i is the index of the key
        k = self.a[i]
        iparent = i // 2  # index of the parent key

        # No sentinal  - while (iparent >= 1 && self.a[iparent] < k
        while self.a[iparent] < k:
            self.a[i] = self.a[iparent]
            i = iparent
            iparent = i // 2

        self.a[i] = k

    def delete_root(self):
        if self.n == 0:
            raise HeapEmptyError("Heap is empty")

        maxValue = self.a[1]
        self.a[1] = self.a[self.n]
        self.n -= 1
        self.restore_down(1)

        return maxValue

    def restore_down(self, i):  # index of the key that needs to be placed in correct location
        k = self.a[i]
        lchild = 2 * i
        rchild = 2 * i + 1

        while rchild <= self.n:
            if k >= self.a[lchild] and k >= self.a[rchild]:
                self.a[i] = k
                return
            else:
                if self.a[lchild] > self.a[rchild]:
                    self.a[i] = self.a[lchild]
                    i = lchild
                else:
                    self.a[i] = self.a[rchild]
                    i = rchild
            lchild = 2 * i
            rchild = lchild + 1

        # If number of nodes is even there is one node that does not have a rchild
        if lchild == self.n and k < self.a[lchild]:
            self.a[i] = self.a[lchild]
            i = lchild
        self.a[i] = k

        # display the heap tree

    def display(self):
        if self.n == 0:
            raise HeapEmptyError("Heap is empty")
        print("Heap size = ", self.n)
        for i in range(1, self.n):
            print(self.a[i], end=" ")
        print()


if __name__ == '__main__':
    heap1 = Heap(13)
    heap1.insert(20)
    heap1.insert(33)
    heap1.insert(15)
    heap1.insert(6)
    heap1.insert(40)
    heap1.insert(60)
    heap1.insert(45)
    heap1.insert(16)
    heap1.insert(75)
    heap1.insert(160)
    heap1.insert(756)
    heap1.insert(123)

    heap1.display()
    heap1.delete_root()
    heap1.display()
    while False:
        print("1. Insert")
        print("2. Delete root")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the value to be inserted: "))
            heap1.insert(value)
        elif choice == 2:
            print("Max valye is ", h.delete_root())
        elif choice == 3:
            heap1.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice.")
