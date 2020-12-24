# Another version of Postfix evaluation
from Stack1 import Stack


def postfix_evaluation(postfix_expr):
    # Create an empty stack
    st = Stack()

    # Traverse the expression
    for symbol in postfix_expr:
        if symbol.isdigit():
            st.push(int(symbol))
        else:
            x = st.pop()
            y = st.pop()

            if symbol == '+':
                st.push(y + x)
            elif symbol == '-':
                st.push(y - x)
            elif symbol == '*':
                st.push(y * x)
            elif symbol == '/':
                st.push(y / x)
            elif symbol == '%':
                st.push(y % x)
            elif symbol == '^':
                st.push(y ** x)
    return st.pop()
