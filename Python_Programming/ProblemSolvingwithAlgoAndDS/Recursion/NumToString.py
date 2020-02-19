def toString(num, base):
    num_to_string = '0123456789ABCDEF'
    if num < 10:
        return num_to_string[num]
    else:
        return toString(num // base, base) + num_to_string[(num % base)]


if __name__ == '__main__':
    print(toString(10, 2))
