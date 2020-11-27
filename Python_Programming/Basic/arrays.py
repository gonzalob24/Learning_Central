import collections
import copy

# arr = [1,2,3,4,5]

# arr2 = arr

# print(arr)
# print(f'array 2: {arr2}')

# arr2[-1] = 22
# print(f'array 2: {arr2}')
# print(f'array 1: {arr}')


# x = 2
# y = x
# y = 10

# print(f'x: {x}\ny: {y}')

# arr3 = arr.copy()
# print(f'array 3: {arr3}')
# arr3[-1] = 88
# print(f'array 3: {arr3}')

# new_arr = [[1,2,3], [4,5,6]]
# print(f'new_array: {new_arr}')
# new_arr2 = new_arr.copy()
# print(f'new_array2: {new_arr2}')
# new_arr2[0][-1] = 33
# print(f'new_array: {new_arr}')
# print(f'new_array2: {new_arr2}')
# print('\n\n----------------Deep Copy----------')
# new_arr_deep = [[11,12,13], [14,15,16]]
# print(f'new_array_deep: {new_arr_deep}')
# new_arr2_deep = copy.deepcopy(new_arr_deep)
# print(f'new_array2_deep: {new_arr2}')
# new_arr2_deep[0][-1] = 33
# print(f'new_array_deep: {new_arr_deep}')
# print(f'new_array2_deep: {new_arr2_deep}')

# print(c)

def arrangeElements(arr, pivot_index):
    """
    Space complexity is at O(1) but time complexity is at O(n^2)
    """
    pivot = arr[pivot_index]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            # look for smaller elements less than pivot
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
        
        # Second pass to group larger elements than pivot
        for i in reversed(range(len(arr))):
            if arr[i] < pivot:
                break
            for j in reversed(range(i)):
                if arr[j] > pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    break
        
        return arr

print(arrangeElements([14,1,11,2,3,15, 7], 4))