def check(array, start, end):
    if start == len(array):
        return end == 0

    if end < 0:  # Never found a closing parenthesis
        return False

    if array[start] == "(":
        return check(array, start + 1, end + 1)

    if array[start] == ")":
        return check(array, start + 1, end - 1)

    return False


print(check(['(', '(', ')', ')', '(', ')'], 0, 0))
