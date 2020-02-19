from Stack1 import Stack
num_string_stack = Stack()  # Create an empty stack


def to_string(n, base):
    num_to_String = '0123456789ABCDEF'

    while n > 0:
        if n < base:
            num_string_stack.push(num_to_String[n])
        else:
            num_string_stack.push(num_to_String[n % base])
        n = n // base

    result = ''
    while not num_string_stack.is_empty():
        result = result + str(num_string_stack.pop())
    return result


if __name__ == '__main__':
    print(to_string(10, 2))
