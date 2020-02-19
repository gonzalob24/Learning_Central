def recursion(num_list):
    if len(num_list) == 1:  # Escape clause
        return num_list[0]
    else:
        return num_list[0] + recursion(num_list[1:])


if __name__ == '__main__':
    first = [1, 2, 3, 4, 5, 6]
    print(recursion(first))
