
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Can't multiply strings")


try:
    x = 5
    y = 0
    z = x / y
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")
finally:
    print("All Done")


def ask():

    while True:
        try:
            n = int(input("Input an integer: "))
            print("Thank you, your number squared is: {}".format(n**2))
        except:
            print("An Error occured! Please Try again!")
            continue
        else:
            print("Thank you")
            break

ask()
