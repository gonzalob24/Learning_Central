from Deque import Deque


def palindrome_checker(strng):
    char_deque = Deque()  # Create a an empty deque to place each character

    for ch in strng:
        char_deque.add_rear(ch)
    # print(char_deque.display())
    palindrome = True

    while char_deque.size() > 1 and palindrome:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()

        if first != last:
            palindrome = False

    return palindrome


if __name__ == '__main__':
    print(palindrome_checker('lsdkjfskf'))
    print(palindrome_checker('radar'))
