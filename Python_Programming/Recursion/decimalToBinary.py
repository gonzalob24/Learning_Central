def dtob(num):
    # to convert to binary simply continue dividing by 2
    if num <= 1:
        return f'{num}'

    remainder = num % 2
    return dtob(num // 2) + str(remainder)


print(dtob(0))
print(dtob(11))
