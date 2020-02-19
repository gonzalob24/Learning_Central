def binary_search(list1, item):
    first = 0
    last = len(list1) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if list1[midpoint] == item:
            found = True
        else:
            if item < list1[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def binary_search_recursion(list1, item):
    if len(list1) == 0: # Because I have an empty list
        return False
    else:
        midpoint = len(list1) // 2
        if list1[midpoint] == item:
            return True
        else:
            if item < list1[midpoint]:
                return binary_search_recursion(list1[:midpoint], item)
            else:
                return binary_search_recursion(list1[midpoint + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print("Binary Search Test")
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
print("\nBinary Search with recursion Test")
print(binary_search_recursion(testlist, 3))
print(binary_search_recursion(testlist, 13))
