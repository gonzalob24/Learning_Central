def find_pair(lst):
    results = []
    memo = {}

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            current_sum = lst[i] + lst[j]
            if current_sum not in memo:
                memo[current_sum] = lst[i], lst[j]

            else:
                strored_sum = memo[current_sum]

                results.append(strored_sum)
                results.append([lst[i], lst[j]])
                return results
    return - 1


print(find_pair([3, 4, 7, 1, 12, 9, 0]))
