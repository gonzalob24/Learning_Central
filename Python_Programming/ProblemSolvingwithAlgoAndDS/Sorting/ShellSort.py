# We need to create h sublist's that will be sorted using insertion sort
# Increments that are relatively prime are good
# hi = 1l hi+1 = 3hi + 1


def shell_sort(array):
    h = int(input("Enter max increment \"h\" (odd number): "))

    while h >= 1:
        for i in range(h, len(array)):
            temp = array[i]
            j = i - h
            while j >= 0 and array[j] > temp:
                array[j + h] = array[j]
                j -= h
            array[ j + h] = temp
        h -= 2

