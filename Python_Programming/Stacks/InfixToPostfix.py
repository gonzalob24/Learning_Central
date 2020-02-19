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

    operator_stack = Stack()  # Empty stack for the operators
    postfixList = []         # Empty stack for the post fix list
    tokenList = infix_expr.split()  # Lets split the expression

    # Lets read each token
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            # Append token to the postfixList
            postfixList.append(token)
        elif token == '(':
            # Push the token to operator stack
            operator_stack.push(token)
        elif token == ')':
            # pop last item from operator stack
            topToken = operator_stack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = operator_stack.pop()
        else:
            while (not operator_stack.is_empty()) and (prec[operator_stack.peek()] >= prec[token]):
                postfixList.append(operator_stack.pop())
            operator_stack.push(token)

    while not operator_stack.is_empty():
        postfixList.append(operator_stack.pop())
    return " ".join(postfixList)


print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))

