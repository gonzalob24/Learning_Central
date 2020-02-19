
def longest_substring(text):
    result = ''
    cur_max = ''
    for i in range(1, len(text)):
        prev_ch = text[i - 1]
        cur_ch = text[i]
        item_index = 0
        if (prev_ch == cur_ch) or (prev_ch in result) or (cur_ch in result) or (cur_max >= result):
            if cur_ch in result:
                item_index += result.index(cur_ch)
            elif prev_ch in result:
                item_index += result.index(prev_ch)
            else:
                item_index = - 1

            if prev_ch not in result:
                result = result + prev_ch

            if len(cur_max) < len(result) and text[-1] not in cur_max:
                cur_max = result

            result = result[item_index + 1:]

        else:
            result = result + prev_ch
    if text[-1] not in cur_max:
        cur_max += text[-1]


    print(cur_max)
    #return cur_max


if __name__ == '__main__':

    # longest_substring('abacdeab')
    #
    longest_substring('ABDEFGABEF')
    #
    # longest_substring('abcaafahbaabdfgz')
    longest_substring('GEEKSFORGEEKS')
    longest_substring('abacde')



