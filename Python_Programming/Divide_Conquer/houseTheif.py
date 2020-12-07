"""
given n houses with value of money in each house. A thief will steal the max value of these houses
- cant steal from two adjacent houses
- what is the max value that I can steal.
"""


def maxStolenValue(house_value_arr, current_index):
    # base condition
    if current_index >= len(house_value_arr):
        return 0

    stealCurrentHouse = house_value_arr[current_index] + \
        maxStolenValue(house_value_arr, current_index + 2)
    skipCurrentHouse = maxStolenValue(house_value_arr, current_index + 1)

    return max(stealCurrentHouse, skipCurrentHouse)


print(maxStolenValue([6, 7, 1, 30, 8, 2, 4], 0))
# print(maxStolenValue([20, 5, 1, 13, 6, 11, 40], 0))
