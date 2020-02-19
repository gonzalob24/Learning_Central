# The first example, we will merge two sorted array into a third array


def merge(a1, a2, temp):
    i = 0
    j = 0
    k = 0
    n1 = len(a1)
    n2 = len(a2)

    while i <= n1 - 1 and j <= n2 - 1:
        if a1[i] < a2[j]:
            temp[k] = a1[i]
            i += 1
        else:
            temp[k] = a2[j]
            j += 1
        k += 1

    # Copying remaining elements of a1 because list a2 is empty
    while i <= n1 - 1:
        temp[k] = a1[i]
        i += 1
        k += 1

    # Copy remaining elements of a2 because list a1 is empty
    while j <= n2 - 1:
        temp[k] = a2[j]
        j += 1
        k += 1


# An array that has two sorted parts and we will need to merge sort
# elements to a new sorted array.
# We need to know the upper bounds of the first array "a"
def merging_to_new_array(a, temp, low1, up1, low2, up2):
    i = low1
    j = low2
    k = low1

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


def sort(a, temp, low, up):
    if low == up:  # Only one element terminating condition
        return

    mid = (low + up) // 2  # integer division

    sort(a, temp, low, mid)  # Sort a[low]...a[mid]
    sort(a, temp, mid + 1, up) # Sort a[mid + 1]...a[up]

    # Merge a[low]...a[mid] and a[mid + 1]...a[up] to temp[low[...temp[up]
    merging_to_new_array(a, temp, low, mid, mid + 1, up)

    # Copy temp[low]..temp[up] to a[low]...a[up]
    copy(a, temp, low, up)


def merge_sort(a):
    n = len(a)
    temp = [None]*n
    sort(a, temp, 0, n - 1)


def copy(a, temp, low, up):
    for i in range(low, up + 1):
        a[i] = temp[i]
