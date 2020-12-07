def knapsackAux(profits_arr, weights_arr, capacity, current_index):
    # base case
    if capacity <= 0 or current_index < 0 or current_index >= len(profits_arr):
        return 0

    profit1 = 0
    # take current element
    if weights_arr[current_index] <= capacity:
        profit1 = profits_arr[current_index] + knapsackAux(
            profits_arr, weights_arr, capacity - weights_arr[current_index], current_index + 1)
    profit2 = knapsackAux(
        profits_arr, weights_arr, capacity, current_index + 1)

    return max(profit1, profit2)


print(knapsackAux([31, 26, 72, 17], [3, 1, 5, 2], 7, 0))
