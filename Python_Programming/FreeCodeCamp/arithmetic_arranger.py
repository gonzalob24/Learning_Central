def arithmetic_arranger(problems, show_answer = False):
    """Basic calculator (+) and (-) 
    There are 4 spaces between each problem

    Args:
        problems ([list]): [list of strings in correct format for addition and subtraction]
        show_answer (bool, optional): [If True display answers]. Defaults to False.

    Returns:
        [arranged_problems]: [if show_answer is True I will display the formatted answers to the user]
    """
    split_problem = problems[0].split(" ")
    top = split_problem[0]
    operator = split_problem[1]
    bottom = split_problem[2]
    dash_length = max(len(top), len(bottom)) + 2
    print("{:>{}}".format(top, dash_length))
    print("{} {:>{}}".format(operator, bottom, dash_length-2))
    print("-"*dash_length)

    # return arranged_problems

arithmetic_arranger(["323244 + 10012"])