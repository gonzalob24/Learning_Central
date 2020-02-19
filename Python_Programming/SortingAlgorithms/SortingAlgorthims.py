def selection_sort(a):
    for i in range(len(a) - 1):  # Passes of the selection sort
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        if i != min_index:
            a[i], a[min_index] = a[min_index], a[i]  # Swapping occurs here if i is not equal to min_index
            # Swapping without the use of a temp variable


def bubble_sort(a):
    for x in range(len(a) - 1, 0, -1):  # From length a -1 to 0 decrement by 1
        swaps = 0
        for j in range(x):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
        if swaps == 0:
            break


def insertion_sort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j = j - 1       # Decrement j
        a[j + 1] = temp


def shell_sort(a):
    h = int(input("Enter max increment(odd value) : "))
    while h >= 1:
        for i in range(h, len(a)):
            temp = a[i]
            j = i - h
            while j >= 0 and a[j] > temp:
                a[j + h] = a[j]
                j = j - h
            a[j + h] = temp
        h = h - 2

# Merging sorted parts of an array into another array
def merge(a, temp, low1, up1, low2, up2):
    i = low1
    j = low2
    k = low1
    # n1 = len(a)
    # n2 = len(a)

    while i <= up1 and j <= up2:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1

    # Copy remaining elements of a1 if list a2 is finished.
    # Remember both lists do not need to be the same size
    while i <= up1:
        temp[k] = a[i]
        i += 1
        k += 1

    # Copy remaining elements of a2 if list a1 is finished
    while j <= up2:
        temp[k] = a[j]
        j += 1
        k += 1

# uses divide and conquer technique
def merge_sort(a):
    n = len(a)
    temp = [None]*n
    sort(a, temp, 0, n - 1)

# Recursive sort
def sort(a, temp, low, up):
    if low == up:  # Only one element
        return

    mid = (low + up) // 2  # integer division

    # Dividing into two sublists
    sort(a, temp, low, mid)  # Sort a[low]...a[mid]
    sort(a, temp, mid + 1, up) # Sort a[mid + 1]...a[up]

    # Merge a[low]...a[mid] and a[mid + 1]...a[up] to temp[low[...temp[up]
    merge(a, temp, low, mid, mid + 1, up)

    # Copy temp[low]..temp[up] to a[low]...a[up]
    copy(a, temp, low, up)

# Copy temp[low]..temp[up] to a[low]...a[up]
def copy(a, temp, low, up):
    for i in range(low, up + 1):
        a[i] = temp[i]

        
def quick_sort(a):
    q_sort(a, 0, len(a) - 1)


def q_sort(a, low, up):   # Recursive sort
    if low >= up:   # Zero or one element in sublist
        return
    p = partition(a, low, up)
    q_sort(a, low, p - 1)    # Sort left sublist
    q_sort(a, p + 1, up)     # Sort right sublist


def partition(a, low, up):
    pivot = a[low]
    i = low + 1     # moves from left to right
    j = up          # moves from right to left

    while i <= j:
        while a[i] < pivot and i < up:
            i += 1
        while a[j] > pivot:
            j -= 1

        if i < j:   # swap a[i] and a[j]
            temp = a[i]
            a[j] = temp
            i += 1
            j -= 1
        else:   # found proper place for pivot
            break

    # Proper place for pivot is j
    a[low] = a[j]
    a[j] = pivot

    return j


list1 = [6, 3, 1, 5, 9, 8]
shell_sort(list1)
print(list1)
