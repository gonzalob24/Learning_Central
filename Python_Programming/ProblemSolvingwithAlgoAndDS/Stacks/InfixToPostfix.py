from Stack1 import Stack


def infix_to_postfix(infix_expr):
    # Prec holds the precedence
    prec = {}
    prec['**'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    # print(prec)
    operand_stack = Stack()         # Empty stack for the operands
    postfixList = []                # Empty stack for the post fix list
    tokenList = infix_expr.split()  # Lets split the expression

    # Lets read each token
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            # Append token to the postfixList
            postfixList.append(token)
        elif token == '(':
            # Push the token to operand stack
            operand_stack.push(token)
        elif token == ')':
            # pop last item from operand stack
            topToken = operand_stack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = operand_stack.pop()
        else:
            while (not operand_stack.is_empty()) and (prec[operand_stack.peek()] >= prec[token]):
                postfixList.append(operand_stack.pop())
            operand_stack.push(token)

    while not operand_stack.is_empty():
        postfixList.append(operand_stack.pop())
    return " ".join(postfixList)


print(infix_to_postfix("( A * ( B + C ) * D )"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("A * B + C * D"))

