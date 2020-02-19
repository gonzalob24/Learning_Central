from Stack1 import Stack


def postfix_eval(postfix_expr):
    operand_stack = Stack()
    tokenList = postfix_expr.split()

    for token in tokenList:
        if token in '0123456789':  # isdigit()
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop() # The last number popped is the second operand
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else: # op == -
        return op1 - op2


if __name__ == '__main__':
    print(postfix_eval('7 8 + 3 2 + /'))
