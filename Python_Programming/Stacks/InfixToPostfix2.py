# Another slight version of infix to postfix


from Stack1 import Stack


def infix_2_postfix(infix_expr):
    postfix = ""    # empty string where operands operators and popped items from stack will go
    operator_stack = Stack()  # Empty stack to push items

    for symbol in infix_expr:
        if symbol == " " or symbol == '\t':  # Ignore white spaces
            continue

        if symbol == '(':
            operator_stack.push(symbol)
        elif symbol == ')':
            top_symbol_stack = operator_stack.pop()
            while top_symbol_stack != '(':
                postfix += top_symbol_stack
                top_symbol_stack = operator_stack.pop()
        elif symbol in '+-*/%^':
            while not operator_stack.is_empty() and precedence(operator_stack.peek()) >= precedence(symbol):
                # If the precedence in the stack is >= scanned symbol pop from stack and add to postfix list
                postfix += operator_stack.pop()
            operator_stack.push(symbol)  # When finished push the scanned symbol
        else:  # Its an operand add it to postfix string
            postfix += symbol

    while not operator_stack.is_empty():
        postfix += operator_stack.pop()
    return postfix


def precedence(symbol):
    if symbol == '(': # Only the left hand parenthesis is in the stack
        return 0
    elif symbol in '+-':
        return 1
    elif symbol in '*/%':
        return 2
    elif symbol == '^':
        return 3
    else:
        return 0


