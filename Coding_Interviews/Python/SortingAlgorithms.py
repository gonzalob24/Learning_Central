class SortingAlgos:

    def inserttion_sort(self, array):
        for i in range(1, len(array)):
            temp = array[i]
            j = i - 1  # first element of array

            while j >= 0 and array[j] > temp:
                array[j + 1] = array[j]  # moves the biggest element to the right
                j -= 1
            array[j + 1] = temp

        return array


if __name__ == "__main__":
    arr1 = [1, 5, 4, 2, 0]
    arr2 = ['D', 'A', 'Z', 'B', 'F']
    algo = SortingAlgos()
    print(algo.inserttion_sort(arr1))
    print(algo.inserttion_sort(arr2))

