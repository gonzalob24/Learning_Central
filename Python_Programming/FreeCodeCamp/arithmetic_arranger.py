def arithmetic_arranger(problems, show_answer = False):
    """Basic calculator (+) and (-) 
    There are 4 spaces between each problem

    Args:
        problems ([list]): [list of strings in correct format for addition and subtraction]
        show_answer (bool, optional): [If True display answers]. Defaults to False.

    Returns:
        [arranged_problems]: [if show_answer is True I will display the formatted answers to the user]
    """
    if len(problems) > 5:
        return "Error: Too many problems."
    top_string = ""
    bottom_string = ""
    dashes_string = ""
    answer = ""
    for problem in problems:
        problem = problem.split(' ')
        if not (problem[0].isdigit()) or not (problem[2].isdigit()):
                return "Error: Numbers must only contain digits."
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        dashes = max(len(problem[0]), len(problem[2])) + 2
        top_string += "{}{}".format(problem[0], " "*(dashes - len(problem[0]) + 2))
        bottom_string += "{} {}{:<7}".format(problem[1], " "*(dashes-len(problem[2]) - 2), problem[2])
        dashes_string += "{}{}".format("-"*dashes, " "*4)
        number = 0

        if problem[1] == '+':
            number = int(problem[0]) + int(problem[2])
        elif problem[1] == "-":
            number = int(problem[0]) - int(problem[2])
        else:
            return "Error: Operator must be '+' or '-'."

        answer += "{:>{}}    ".format(str(number), dashes)
    arranged_problems = top_string + "\n" + bottom_string + "\n" + dashes_string
    if show_answer:
        return arranged_problems + "\n" + answer
    else:
        return arranged_problems


print(arithmetic_arranger(["332 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))

