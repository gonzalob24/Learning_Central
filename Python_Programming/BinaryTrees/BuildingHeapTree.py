
class HeapEmptyError(Exception):
    pass


# class Heap:

# def __init__(self, maxSize = 20):
#     self.a =[None] * maxSize
#     self.n = 0
#     self.a[0] = 99999  # all values in the heap should be less than this value

# def insert(value):
#     self.n += 1  # increment the size of the heap
#     self.a[self.n] = value
#     self.restore_up(self.n) # this places the key in its proper place

def build_heap_top_down(a_heap, n_length):
    for i in range(2, n_length + 1):
        restore_up(i, a_heap)


def build_heap_bottom_up(a_heap, n_length):
    i = n_length // 2
    while i >= 1:
        restore_down(i, a_heap, n_length)
        i = i - 1


def restore_up(i, a):  # i is the index of the key
    k = a[i]
    iparent = i // 2  # index of the parent key

    while a[iparent] < k:  # No sentinal  - while (iparent >= 1 && self.a[iparent] < k
        a[i] = a[iparent]
        i = iparent
        iparent = i // 2

    a[i] = k


# def delete_root(self):
#     if self.n == 0:
#         raise HeapEmptyError("Heap is empty")
#
#     maxValue = self.a[1]
#     self.a[1] = self.a[self.n]
#     self.n -= 1
#     self.restore_down(1)
#
#     return maxValue

def restore_down(i, a, n):  # index of the key that needs to be placed on correct location
    k = a[i]
    lchild = 2 * i
    rchild = lchild + 1

    while rchild <= n:
        if k >= a[lchild] and k >= a[rchild]:
            a[i] = k
            return
        else:
            if a[lchild] > a[rchild]:
                a[i] = a[lchild]
                i = lchild
            else:
                a[i] = a[rchild]
                i = rchild
        lchild = 2 * i
        rchild = lchild + 1

    # If number of nodes is even there is one node that does not have a rchild
    if lchild == n and k < a[lchild]:
        a[i] = a[lchild]
        i = lchild
    a[i] = k

    # display the heap tree
# def display():
#     if .n == 0:
#         raise HeapEmptyError("Heap is empty")
#         return
#     print("Heap size = ", self.n)
#     for i in range(1, self.n):
#         print(self.a[i], end=" ")
#     print()


if __name__ == '__main__':

    heap1 = [99999, 20, 33, 15, 6, 40, 60, 45, 16, 75, 10, 80, 12]

    n1 = len(heap1) - 1
    build_heap_bottom_up(heap1, n1)
    for i in range(1, n1 + 1):
        print(heap1[i], end=" ")
    print()

    heap2 = [99999, 20, 33, 15, 6, 40, 60, 45, 16, 75, 10, 80, 12]
    n2 = len(heap1) - 1
    build_heap_top_down(heap2, n2)
    for i in range(1, n2 + 1):
        print(heap2[i], end=" ")
    print()
