from Stack1 import Stack


def divide_by_two(number):
    remainder_stack = Stack() # Create an empty stack

    while number > 0:
        remainder = number % 2
        remainder_stack.push(remainder)
        number = number // 2
   # remainder_stack.display()  Prints the stack in list form
    result = ''
    while not remainder_stack.is_empty():
        result = result + str(remainder_stack.pop())
    return result


# We need a more general case
def base_conversion(number, base):
    digits = '0123456789ABCDEF'
    remainder_stack = Stack()

    while number > 0:
        remainder = number % base
        remainder_stack.push(remainder)
        number = number // base

    result = ''
    while not remainder_stack.is_empty():
        result = result + str(digits[remainder_stack.pop()])

    return result


if __name__ == '__main__':
    print(divide_by_two(42))
    print(base_conversion(25, 16))
