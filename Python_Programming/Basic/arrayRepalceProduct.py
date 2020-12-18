def replaceWithProduct(array):
    product = array[0]
    for i in range(1, len(array)):
        product *= array[i]

    for i, item in enumerate(array):
        array[i] = product//item

    return array


print(replaceWithProduct([1, 2, 3, 4]))
