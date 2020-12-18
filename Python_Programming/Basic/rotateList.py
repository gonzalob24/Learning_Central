def rotate(array, n):
    return (array[-n:] + array[0:-n])


print(rotate([1, 2, 3, 4], 2))
print(rotate(['13', 'a', 'Python'], 2))
