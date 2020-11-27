def bubbleSort(arr):
    """
    When to use:
        - array is sorted
        - space is a concer
    
    When not to use:
        - this algorithm runs in O(n^2) Time O(1) space
    """

    # get leght of array
    n = len(arr)

    # use two loops
    for i in range(n):
        for j in range(n - i -1):
            if (arr[j] > arr[j + 1]):
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [4,10,11,1,30,2,15,0]

arr_sorted = bubbleSort(arr)
print(f'Bubble sort: \t{arr_sorted}')

def insertionSort(arr):
    """

    """
    n = len(arr)

    for i in range(n):
        # set index_of_min = 0
        idx_of_min = i
        for j in range(i + 1, n):
            # look for smaller element that is small than element
            # at index_of_min
            if arr[j] < arr[idx_of_min]:
                idx_of_min = j
        if idx_of_min != i:
            arr[idx_of_min], arr[i] =  arr[i], arr[idx_of_min]
    
    return arr

arr2 = [4,10,11,1,30,2,15,0]

sorted_arr2 = insertionSort(arr2)
print(f'Insertion sort: {sorted_arr2}')