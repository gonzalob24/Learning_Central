def permutations(elements):
    if len(elements) == 0:
        return [[]]

    firstEL = elements[0]
    restEL = elements[1:]

    allPermutations = []
    permsWithoutFirstEl = permutations(restEL)
    for singlePerm in permsWithoutFirstEl:
        for i in range(len(singlePerm) + 1):
            permWithFirstEL = [*singlePerm[0:i], firstEL, *singlePerm[i:]]
            allPermutations.append(permWithFirstEL)

    return allPermutations


print(permutations(["a", "b", "c"]))
