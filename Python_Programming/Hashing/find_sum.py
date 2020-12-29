def find_sum(lst, k):
    # lst --> lst
    # k  --> a sum of two integers

    # run time: 0(n2)
    # for i in range(len(lst)): # --> n
    #     for j in range(i+1, len(lst)): # --> n
    #         current_sum = lst[i] + lst[j]
    #         if current_sum == k:
    #             return [lst[i], lst[j]]
    # return []
    memo = {}
    for item in lst:
        difference = k - item

        if difference not in memo:
            memo[item] = difference

        else:
            return [difference, memo[difference]]


print(find_sum([1, 21, 3, 14, 5, 60, 7, 6], 81))

print(find_sum([1, 3, 2, 4], 6))
