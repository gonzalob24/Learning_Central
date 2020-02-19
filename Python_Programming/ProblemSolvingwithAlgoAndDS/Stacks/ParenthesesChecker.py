from Stack1 import Stack


def par_checker(symbol_strng):
    s = Stack()     # Empty stack to place parentheses
    balanced = True
    index = 0

    while index < len(symbol_strng) and balanced:
        symbol = symbol_strng[index]     # First parentheses is at index 0
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top_open = s.pop()
                if not matches(top_open, symbol):
                    balanced = False
        index += 1

    return balanced and s.is_empty()

    # if balanced and s.is_empty():
    #     return True
    # else:
    #     return False


def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)     # Boolean expression


if __name__ == '__main__':
    print(par_checker('((()))'))
    print(par_checker('(()'))
    print(par_checker('{{([][])}()}'))
    print(par_checker('[)'))
