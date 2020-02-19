# Split list into sorted and unsorted side compare elements and insert in correct order


def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1

        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j]
            j -= 1  # Decrement j insert temp in correct location
        array[j + 1] = temp
