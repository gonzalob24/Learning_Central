def gcd(num1, num2):
    # n1 = []
    # n2 = []
    # for i in range(1, max(num1, num2) + 1):
    #     if num1 >= i:
    #         if num1 % i == 0:
    #             n1.append(i)
    #     if num2 >= i:
    #         if num2 % i == 0:
    #             n2.append(i)
    # print(n1, n2)
    # for i in range(min(len(n1), len(n2)) - 1, 0, -1):

    if num1 == num2:
        return num1

    if num1 > num2:
        return gcd(num1 - num2, num2)

    return gcd(num1, num2 - num1)


print(gcd(6, 9))
