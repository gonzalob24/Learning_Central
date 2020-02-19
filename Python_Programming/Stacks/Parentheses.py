from Stack1 import Stack


def is_valid(expression):
    # Create an empty stack
    par_stack = Stack()

    for ch in expression:
        if ch in '({[':
            par_stack.push(ch)
        if ch in ')}]':
            if par_stack.is_empty():
                print("Right parentheses are more then left parentheses.")
                return False
            else:
                popped_char = par_stack.pop()
                if not matched_parentheses(popped_char, ch):
                    print("Mismatched parentheses are ", popped_char, " and ", ch)
                    return False

    if par_stack.is_empty():
        print("Balanced parentheses")
        return True
    else:
        print("Left parentheses are more than right parentheses")
        return False


def matched_parentheses(leftPar, rightPar):
    if leftPar == '[' and rightPar == ']':
        return True
    if leftPar == '(' and rightPar == ')':
        return True
    if leftPar == '{' and rightPar == '}':
        return True
    return False


if __name__ == '__main__':

    while True:
        print("Enter an expression with parentheses (q to quit): ", end=" ")
        expr = input()

        if expr == 'q':
            break

        if is_valid(expr):
            print("Valid expression")
        else:
            print("Invalid expression")

