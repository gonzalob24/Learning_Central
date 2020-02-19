def selection_sort(list_of_nums):
    for i in range(len(list_of_nums) - 1):
        min_index = i
        for j in range(i + 1, len(list_of_nums)):
            if list_of_nums[j] < list_of_nums[min_index]:
                min_index = j
        if i != min_index:
            list_of_nums[i], list_of_nums[min_index] = list_of_nums[min_index], list_of_nums[i]
