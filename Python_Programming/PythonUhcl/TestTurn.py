import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno #get line number where test took place
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def test_suite():
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == "None")
    test(turn_clockwise("rubbish") == "None")

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

test_suite()