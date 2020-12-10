def combos(elements):
    # base case
    if len(elements) == 0:
        return [[]]

    # recursive case
    firstEl = elements[0]  # take or not take the element
    restEL = elements[1:]  # copy the rest of the elements

    combosWithoutFirstEL = combos(restEL)
    # combos with first element
    combosWithFirstEL = []

    for singleComb in combosWithoutFirstEL:
        comboWithFirstEL = [*singleComb, firstEl]
        combosWithFirstEL.append(comboWithFirstEL)

    return [*combosWithoutFirstEL, *combosWithFirstEL]


print(combos(["a", "b", "c"]))
