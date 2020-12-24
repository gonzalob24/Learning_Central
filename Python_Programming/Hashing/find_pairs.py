def find_symmetric(lst):
    pairs = set()
    results = []

    for pair in lst:
        pair_tuple = tuple(pair)
        reversed_pair_tup = tuple(reversed(pair_tuple))

        if reversed_pair_tup in pairs:
            results.append(list(pair_tuple))
            results.append(list(reversed_pair_tup))
        else:
            pairs.add(pair_tuple)
    return results


arr = [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]]
symmetric = find_symmetric(arr)
print(symmetric)

lst = [1, 2]
lst2 = [2, 1]
print(lst)
lst.reverse()
print(lst)
print(tuple(reversed(tuple(lst))))
print(tuple(lst2) == tuple(reversed(tuple(lst))))
