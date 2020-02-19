import sys


def test(did_it_pass, ):
    """  Print the result of a test.  """
    line_number = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_it_pass:
        msg = "Test at line {0} ok.".format(line_number)
    else:
        msg = ("Test at line {0} FAILED.".format(line_number))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)


def absolute_value(n):   # Buggy version
    """ Compute the absolute value of n """
    if n <= 0:
        return -n
    elif n > 0:
        return n


test_suite()        # Here is the call to run the tests
