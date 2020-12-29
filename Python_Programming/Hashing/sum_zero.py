def sum_zero(lst):
    # for i in range(len(lst)):
    #     sublist_sum = lst[i]
    #     for j in range(i+1, len(lst)):
    #         sublist_sum += lst[j]
    #         if sublist_sum == 0:
    #             return True
    # return False

    # Linear time
    memo = {}
    total_sum = 0
    for num in lst:
        total_sum += num

        if num == 0 or total_sum == 0 or memo.get(total_sum) is not None:
            return True
        memo[total_sum] = num
    return False


print(sum_zero([6, 4, -7, 3, 12, 9]))

g = ['g', 'o', 'n']
s = ''

s = s.join(g)
print(s)
print('zz' in s)

string = ['the', 'hello', 'there', 'answer',
          'any', 'educative', 'world', 'their', 'abc']
word = 'helloworld'

test = ''
test = test.join(string)
print(test)
