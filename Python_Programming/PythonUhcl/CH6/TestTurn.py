import sys


def test(did_it_pass):
    line_number = sys._getframe(1).f_lineno  # get line number where test took place
    if did_it_pass:
        msg = "Test at line {0} ok.".format(line_number)
    else:
        msg = "Test at line {0} FAILED.".format(line_number)
    print(msg)


def test_suite():
    print("Turn clockwise test")
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == "None")
    test(turn_clockwise("rubbish") == "None")
    print("\n\nDay name test")
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    print("\n\nDay num test")
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    print("\n\nDay add1")
    test(day_add1("Monday", 4) == "Friday")
    test(day_add1("Tuesday", 0) == "Tuesday")
    test(day_add1("Tuesday", 14) == "Tuesday")
    test(day_add1("Sunday", 100) == "Tuesday")
    print(6 / 4)

# use of a return statement


def turn_clockwise(n):
    if n == "N":
        return "E"
    elif n == "E":
        return "S"
    elif n == "S":
        return "W"
    elif n == "W":
        return "N"
    else:
        return "None"


def day_name(number):
    if number == 0:
        return "Sunday"
    elif number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    elif number == 6:
        return "Saturday"
    else:
        return None


def day_num(name):
    if name == "Sunday":
        return 0
    elif name == "Monday":
        return 1
    elif name == "Tuesday":
        return 2
    elif name == "Wednesday":
        return 3
    elif name == "Thursday":
        return 4
    elif name == "Friday":
        return 5
    elif name == "Saturday":
        return 6
    else:
        return None


def day_add1(day, day_number):
    num = day_num(day)
    day_number = (day_number + num) % 7
    return day_name(day_number)


# turn_clockwise
test_suite()
