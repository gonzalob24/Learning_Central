def pascals(n):
    if n == 0:
        return [1]

    # add 1 to the front
    line = [1]
    # call previous line
    previousLine = pascals(n - 1)

    for i in range(len(previousLine) - 1):
        line.append(previousLine[i] + previousLine[i+1])

    line += [1]

    return line


print(pascals(5))
