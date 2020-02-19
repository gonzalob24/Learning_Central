import math


def autori(name):
    name = input()
    result = name[0]
    for i in range(1, len(name)):
        if name[i] == "-":
            result += name[i + 1]

    print(result)


def squares():
    number = int(input())  # 1 to 15
    n = 0
    for i in range(number + 1):
        n = 2 ** i + 1

    dots = n ** 2
    print(n)
    print(dots)


def user_input():
    while True:
        x = int(input())
        y = int(input())

        if x <= 1000 and y <= 1000:
            break
        else:
            continue

    return (x, y)


def quadrant():
    (x, y) = user_input()

    if x > 0 and y > 0:
        print("1")
    elif x < 0 and y > 0:
        print("2")
    elif x < 0 and y < 0:
        print("3")
    else:
        print("4")


def twostones():
    while True:
        stones = int(input())

        if 1 <= stones <= 10000000:
            if stones % 2 == 0:
                print("Bob")
                break
            else:
                print("Alice")
                break
        else:
            continue


def tarifa():
    x = 0
    n = 0
    p = 0
    # test inputs are correct both x and n are b/t 1 and 100
    while True:
        x = int(input())  # mb given by company each month
        n = int(input())  # n is the number of months

        if 1 <= x <= 100 and 1 <= n <= 100:
            x = x + x * n
            break

    for i in range(1, n + 1):
        while True:
            p = int(input())
            if 0 <= p <= 1000:
                break
        x -= p
    print(x)


def timeloop():
    # N is b/w 1 and 100
    while True:
        n = int(input())
        if 1 <= n <= 100:
            break
    for i in range(1, n + 1):
        print(i, " Abracadabra")


def carrots():
    while True:
        info = input()
        if not (len(info.split())) > 1:
            continue
        info = info.split()
        n = int(info[0])
        p = int(info[1])
        if 1 <= n and p <= 1000:
            break
    for i in range(1, n + 1):
        str = input()
    print(p)


def sibice():
    """
    first line of matches , 1 <= N <=50 number of matches on the floor
        for each line random number  1 - 1000 = length of match
        matches can fit diagonally
    W - 1 <= W <= 100, H 1 <= H <= 100 the dimensions of the box

    DA - match fits
    NE - does not fit
    """
    n = 0
    w = 0
    h = 0
    match_length = []

    while True:
        nlist = input("Number of matches on the floor: ")
        if len(nlist.split()) != 3:
            continue
        nlist = nlist.split()
        n = int(nlist[0])
        w = int(nlist[1])
        h = int(nlist[2])

        if 1 <= n <= 50 and 1 <= h <= 100 and 1 <= w <= 100:
            diag = math.sqrt(w ** 2 + h ** 2)
            for i in range(1, n + 1):
                while True:
                    ml = int(input("Match length: "))
                    if 1 <= ml <= 1000:
                        if ml <= diag:
                            print("DA")
                        else:
                            print("NE")
                        break
            break


def bijele():
    """
    6 integers in one line each b/w 0 - 10 (inclusive)
    kings, queens, rooks, bishops, knights and pawns
    """
    while True:
        nlist = input()
        if len(nlist.split()) != 6:
            continue
        nlist = nlist.split()
        kings = int(nlist[0])
        queens = int(nlist[1])
        rooks = int(nlist[2])
        bishops = int(nlist[3])
        knights = int(nlist[4])
        pawns = int(nlist[5])

        if not (
                0 <= kings <= 10 and 0 <= queens <= 10 and 0 <= rooks <= 10 and 0 <= bishops <= 10 and 0 <= knights <= 10 and 0 <= pawns <= 10):
            continue
        else:

            print(1 - kings, end=" ")

            print(1 - queens, end=" ")

            print(2 - rooks, end=" ")

            print(2 - bishops, end=" ")

            print(2 - knights, end=" ")

            print(8 - pawns)

            break


def r2():
    """
    s --> mean of r1 and r2. s = (r1 + r2)/2  r2 = s * 2 - r1
    s and r1 b.w -1000 and 1000

    """
    while True:
        nlist = input()
        if len(nlist.split()) != 2:
            continue
        nlist = nlist.split()
        r1 = int(nlist[0])
        s = int(nlist[1])
        if abs(max(s, r1)) >= 1000:
            continue
        else:
            r2 = s * 2 - r1
            print(r2)
            break


def pot():
    """
    input n--. 1-10
        p -- 10<= p <= 9999
    """
    while True:
        n = input()
        if not (n.isdigit()):
            continue
        if not (1 <= int(n) <= 10):
            continue
        n = int(n)
        total = 0
        for i in range(1, n + 1):
            while True:
                p = input()
                if not (p.isdigit()):
                    continue
                if not (10 <= int(p) <= 9999):
                    continue
                else:
                    n = int(p[:len(p) - 1])
                    pow = int(p[-1])
                    total = total + n ** pow
                    break
        print(total)
        break


def nast_hacks():
    """
    1 <= n <= 100
        -10^6 <= r (revenue no adds) e ≤ 10^6 (revenue with adds) 0 <= c (cost of adds) <= 10^6
    """
    while True:
        r = 0
        e = 0
        c = 0
        n = input()
        if not (n.isdigit()) or not (1 <= int(n) <= 100):
            continue
        n = int(n)

        for case in range(1, n + 1):
            while True:
                data = input()
                if len(data.split()) != 3:
                    continue
                data = data.split()
                r = int(data[0])
                e = int(data[1])
                c = int(data[2])

                if not (-10 ** 6 <= int(r) or not (int(e) <= 10 ** 6) or not (0 <= int(c) <= 10 ** 6)):
                    continue
                e -= c
                if r > e:
                    print("do not advertise")
                elif r == e:
                    print("does not matter")
                else:
                    print("advertise")
                break
        break


def speed_limit():
    """
    total distance driven
    1 <= n <= 10
       1 <= s (speed) <= 90   1 <= t (total elapsed time) <= 12
       -1 ends input
    :return:
    """

    while True:
        n = input("Enter value for n: ")
        if int(n) == -1:
            break
        if not (n.isdigit()) or not (1 <= int(n) <= 12):
            continue
        n = int(n)
        total_miles = 0
        prev_time = 0
        for number in range(1, n + 1):
            while True:
                data = input("Enter speed and time: ")
                if len(data.split()) != 2:
                    continue

                data = data.split()
                s = int(data[0])
                t = int(data[1])
                if not (1 <= s <= 90) or not (1 <= t <= 12):
                    continue
                elapsed_time = t - prev_time
                prev_time = t
                total_miles += (s * elapsed_time)
                break
        print(total_miles, " miles")


def last_factorial_digit():
    """
    N! = N*(n -1)...1

    1 <= T (Test cases) <= 10
        N is at most 10 (most if can be is 10)

    :return:
    """

    while True:
        t = input("Number of test cases: ")
        if not (t.isdigit()) or not (1 <= int(t) <= 10):
            continue

        t = int(t)

        for case in range(t):
            while True:
                n = input()

                if not (n.isdigit()) or not (0 <= int(n) <= 10):
                    continue

                n = int(n)
                print(math.factorial(n) % 10)
                break
        break


def judging_moose():
    """
    0 <= l (left tines) <= 20 and 0 <= r (right times) <= 20
    :return:
    """
    while True:
        left_right = input("Enter left and right tines: ")
        if len(left_right.split()) != 2:
            continue
        left_right = left_right.split()
        left = int(left_right[0])
        right = int(left_right[1])

        if not (0 <= left <= 20 and 0 <= right <= 20):
            continue

        if left == right and (left != 0 and right != 0):
            print("Even", left + right)
        elif left != right:
            print("Odd", max(left, right) * 2)
        else:
            print("Not a moose")
        break


def piece_of_cake():
    """
    first line of input has three numbers:
    2 <= n in cm(length of the sides) <= 10 000
    0 < h (distance of horizontal cut from the top) < n
    0 < v (distance of vertical cut from left edge of cake) < n
    :return:
    """
    cake_thickness = 4

    while True:
        data = input()
        data = data.split()
        if len(data) != 3 and not ("".join(data).isdigit()):
            continue

        n = int(data[0])
        h = int(data[1])
        v = int(data[2])

        if not (2 <= n <= 10000) or not (0 < h < n) or not (0 < v < n):
            continue
        h_big_piece = max(h, n - h)
        v_big_piece = max(v, n - v)

        volume_big_piece = v_big_piece * h_big_piece * cake_thickness
        print(volume_big_piece)
        break


def trik():
    """
    input moves  ABC up to 50 random times
    ouput index where ball is
    :return:
    """
    move_options = "ABC"
    while True:
        user_data = input()
        if not (1 <= len(user_data) <= 50):
            continue
        if user_data != user_data.upper():
            continue
        if not (len(set(user_data)) <= 3):
            continue
        set_user_data = "".join(set(user_data))
        for mov in set_user_data.upper():
            if mov not in move_options:
                continue

        user_moves = user_data.upper()
        ball = 1
        for move in user_moves:
            if move == "A" and (ball == 1 or ball == 2):
                if ball == 1:
                    ball = 2
                else:
                    ball = 1
            elif move == "B" and (ball == 2 or ball == 3):
                if ball == 2:
                    ball = 3
                else:
                    ball = 2
            elif move == "C" and (ball == 3 or ball == 1):
                if ball == 3:
                    ball = 1
                else:
                    ball = 3
            else:
                ball = ball

        print(ball)
        break


def human_cannon_ball():
    """
    1 <= n <= 100
        0 < v_not <= 200
        0 < theta < 90
        0 < x1 1000
        0 < h1 < h2 < 1000

        all numbers are floats
    :return:
    """
    while True:
        n = input("Enter the number of cases: ")
        if not (n.isdigit()) or not (1 <= int(n) <= 100):
            continue
        n = int(n)

        for case in range(n):
            while True:
                data = input("Data separated by space (v_not, theta, x1, h1, h2)")
                if not (len(data.split(" ")) == 5):
                    continue

                data = data.split(" ")
                v_not = float(data[0])
                theta = float(data[1])
                x1 = float(data[2])
                h1 = float(data[3])
                h2 = float(data[4])

                if not (0 < v_not <= 200) or not (0 < theta < 90) or not (0 < x1 < 1000) or \
                        not (0 < h1 < h2) or not (h1 < h2 < 1000):
                    continue
                break

            y_t = x1 * math.tan(math.radians(theta)) - 0.5 * 9.81 * (
                    (x1 / (v_not * math.cos(math.radians(theta)))) ** 2)

            if (h1 + 1) < y_t < (h2 - 1):
                print("Safe")
            else:
                print("Not Safe")
        break


def symmetric_coder():
    """
    n (#_sets)
       1 <= n_strings one per line no spaces <= 15
            each string is 1 <= string_size <= 25
    final input contains 0
    :return:
    """
    n_sets = 0
    while True:
        n_sets = input("Enter the number of sets: ")
        if not (n_sets.isdigit()) or not (int(n_sets) >= 1):
            continue
        n_sets = int(n_sets)
        break

    set_length = 0
    for n in range(n_sets):
        while True:
            set_length = input("Enter size of set: ")
            if not (set_length.isdigit()) or not (1 <= int(set_length) <= 15):
                continue
            set_length = int(set_length)
            break

    all_strings = []
    for s in range(int(set_length)):
        while True:
            strng = input("Enter string: ")
            if not (1 <= len(strng) <= 25):
                continue
            all_strings.append(strng)
            break

    for n in range(0, set_length, 2):
        print(all_strings[n])
    for n in range(set_length - 1, 1, -2):
        print(all_strings[n])


def ladder():
    """
    h(wall height)
    v(angle of ladder)
    find height of the ladder

    1 <= h <= 10,000  1<= v <= 89
    :return:
    """
    while True:
        data = input("Enter h and v: ")
        if not (len(data.split()) == 2) or not ("".join(data.split()).isdigit()):
            continue
        data = data.split()
        h = int(data[0])
        v = int(data[1])

        if not (1 <= h <= 10000) or not (1 <= v <= 89):
            continue
        ladder_length = h / math.sin(math.radians(v))
        print(math.ceil(ladder_length))
        break


def railroad():
    """
    0 <= x <= 1000 0 <= y <= 1000
    """
    while True:
        data = input()

        if not (len(data.split()) == 2) or not ("".join(data.split()).isdigit()):
            continue

        data = data.split()
        x = int(data[0])
        y = int(data[1])

        if not (0 <= x <= 1000) or not (0 <= y <= 1000):
            continue

        x_connect = 4 * x
        y_connect = 3 * y

        if (x_connect + y_connect) % 2 != 0:
            print("impossible")
        else:
            print("possible")

        break


def harshad_numbers():
    """
    Harshad a number that is evenly divisible by the sum of its digits.
    :return:
    """

    def sum_n(n):
        harshad_sum = 0
        while n > 0:
            x = n % 10
            n = n // 10
            harshad_sum += x
        return harshad_sum

    while True:
        h_n = input("Enter number: ")
        if not (h_n.isdigit()) or not (0 <= int(h_n) <= 1000000000):
            continue

        h_n = int(h_n)
        sum_h_n = sum_n(h_n)

        while True:
            if h_n % sum_h_n == 0:
                print(h_n)
                break
            else:
                h_n += 1
                sum_h_n = sum_n(h_n)
                continue
        break


def zanzibar():
    """
    1 <= T (test cases)  <= 13

    :return:
    """


def stararrangements():
    """
    3 <= s (stars) <= 32767
    :return:
    """

    def sum_of_x_y(x, y, s):
        sum_x_y = 0
        while sum_x_y < s:
            sum_x_y = sum_x_y + x

            if sum_x_y == s:
                return sum_x_y
            sum_x_y = sum_x_y + y
            if sum_x_y == s:
                return sum_x_y

    while True:
        s = input("Enter the number of stars: ")

        if not (s.isdigit()) or not (3 <= int(s) <= 32767):
            continue

        s = int(s)

        x = 2
        y = 1
        print(s, end=":")
        print()
        while True:
            sum_pairs = sum_of_x_y(x, y, s)
            if sum_pairs == s:
                print(x, end=",")
                print(y)
            if x + y == s or x + y > s:
                break
            else:
                if x > y:
                    y += 1
                elif x == y:
                    x += 1

        break


def kornislav():
    """
    given 4 numbers find the largest area enclosed by a square
    0<𝐴,𝐵,𝐶,𝐷<100
    :return:
    """

    while True:
        data = input("Enter data: ")
        if (len(data.split()) != 4) or not ("".join(data.split()).isdigit()):
            continue

        data = data.split()
        data.sort()
        first = int(data[0])
        sec = int(data[1])
        third = int(data[2])
        fourth = int(data[3])

        if not (0 < first < 100) or not (0 < sec < 100) or not (0 < third < 100) or not (0 < fourth < 100):
            continue

        area = third * first
        print(area)
        break


def kemija():
    """
    add a p after each vowel a e i o u then add vowel again

    write a program that decodes the sentences a space separates words and at most 100 characters
    """
    vowels = "aeiou"
    decoded_sentence = ""

    while True:
        string = input("Enter the sentence: ")

        if (len(string) > 100) or not (string.islower()):
            continue
        i = 0
        while i < len(string):
            if string[i] in vowels:
                i += 2
            decoded_sentence += string[i]
            i += 1
        print(decoded_sentence)
        break


def easiest():
    """
    N * m
    find the smallest positive integer p that has the same sum of the digits when multiplied b N
    Number must be bigger than 10
    1 <= N <= 100 000
    """

    def sum_of_numbers(number):
        total_sum = 0
        while number != 0:
            m = number % 10
            total_sum += m
            number = number // 10
        return total_sum

    while True:
        N = input("Enter test case: ")
        if int(N) == 0:
            break
        if not (N.isdigit()) or not (1 <= int(N) <= 100000):
            continue

        N = int(N)
        p = 11
        sum_of_N = sum_of_numbers(N)
        sum_of_N_p = sum_of_numbers((N * p))

        while sum_of_N_p != sum_of_N:
            p += 1
            sum_of_N_p = sum_of_numbers(N * p)
        print(p)


def cups():
    """
    1 <= N (No. Cups) <= 20
        radius color or color radius
        0 < R < 100
    :return:
    """
    number_of_cups = ""
    radius_color = {}
    while True:
        number_of_cups = input("Enter the No. Cups: ")
        if not (number_of_cups.isdigit()) or not (1 <= int(number_of_cups) <= 20):
            continue
        number_of_cups = int(number_of_cups)
        break

    for i in range(number_of_cups):
        while True:
            cup_info = input("Enter the cup info: ")
            cup_info = cup_info.split()

            if cup_info[0].isdigit() and (0 < (int(cup_info[0]) / 2) < 1000) and cup_info[1].islower():
                radius_color[int(cup_info[0]) / 2] = cup_info[1]
                break
            elif cup_info[0].islower() and cup_info[1].isdigit() and (0 < (int(cup_info[1])) < 1000):
                radius_color[int(cup_info[1])] = cup_info[0]
                break
            else:
                continue

    print(radius_color)
    cup_radius = list(radius_color.keys())
    cup_radius.sort()
    print(cup_radius)
    for radius in cup_radius:
        print(radius_color.get(radius))


def cups2():
    """
    1 <= N (No. Cups) <= 20
        radius color or color radius
        0 < R < 100
    :return:
    """
    from collections import defaultdict

    radius_color = defaultdict(list)
    while True:
        number_of_cups = input("Enter the No. Cups: ")
        if not (number_of_cups.isdigit()) or not (1 <= int(number_of_cups) <= 20):
            continue
        number_of_cups = int(number_of_cups)
        break

    for i in range(number_of_cups):
        while True:
            cup_info = input("Enter the cup info: ")
            cup_info = cup_info.split()
            cup_info.sort()

            if not (cup_info[0].isdigit()) or not (0 < int(cup_info[0]) < 1000) or not (cup_info[1].islower()):
                continue

            if int(cup_info[0]) not in radius_color:
                radius_color[int(cup_info[0])].append(cup_info[1])
            elif int(cup_info[0]) in radius_color and cup_info[1] not in radius_color.get(int(cup_info[0])):
                radius_color[int(cup_info[0])].append(cup_info[1])
            else:
                continue
            break

    print(radius_color)
    cup_radius = list(radius_color.keys())
    cup_radius.sort()
    print(cup_radius)
    for radius in cup_radius:
        for color in radius_color.get(radius):
            print(color)


"""
info = "gray 11"
info = info.split()
info.sort()
print(info)
print(info[0])
n = {11:"red", 5:"blue"}
keyss = list(n.keys())
keyss.sort()
print(keyss)
print(n[keyss[0]] != info[1])
if int(info[0]) not in n:
   n[int(info[0])] = info[1]
elif int(info[0]) in n and n[int(info[0])] != info[1]:
    n[int(info[0])] = info[1]
print(n)
"""


# from collections import defaultdict
#
#
# n = ["10", "red"]
# w = ["red", "10"]
#
# d = defaultdict(list)
# a = "dgreen"
# c = "blue"
# b = "black"
# d[10].append(a)
# d[10].append(c)
# d[15].append(b)
# print(d)
# for k in d.keys():
#     for color in d.get(k):
#         print(color)


def reverserot():
    """
    1 <= T (Test Case) <= 30
        1 <= N <= 27 ---> 1 <= string(only capital letter) <= 40
    """

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

    def check(test_str):
        import re
        pattern = r'[^\_.A-Z]'
        if re.search(pattern, test_str):
            return False
        else:
            return True

    T_cases = 0
    while True:
        T_cases = input("Enter cases: ")
        if not (1 <= int(T_cases) <= 30):
            continue
        T_cases = int(T_cases)
        break

    while True:
        N_strng = input("Enter shift No. and string: ")
        if N_strng == "0":
            break
        N_strng = N_strng.split()
        if not (N_strng[0].isdigit()) or not (1 <= int(N_strng[0]) <= 27):
            continue

        N = int(N_strng[0])
        strng = N_strng[1]

        if not (strng.isupper()) and not (1 <= len(strng) <= 40):
            continue

        if check(strng) is False:
            continue

        strng = strng[::-1]
        results = ""
        for ch in strng:
            idx = alpha.find(ch)
            results += alpha[(idx + N) % 28]
        print(results)
        # T_cases -= 1
        # if T_cases == 0:
        #     print(T_cases)
        #     break


# alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
# s = "ABCD._ABCDFE"
#
# s = s[::-1]
# d = "C" + str(2)
#
# dot = alpha.find(".")
# print(alpha[(dot + 3) % 28])
#
# n_strng = "10 red"
# print(len(n_strng.split()))


def ptice():
    """
    1 <= N (No. of questions on exam) <= 100
        strng of N letters A,B,C the correct question tp the exam

    Output:
        M --> largest number of correct answers
        names of boys who got M correct answers in alphabetical order.
    """
    Adrian = "ABC"
    Bruno = "BABC"
    Goran = "CCAABB"

    def check_for_correct_answers(correct_answers, student_pattern):
        idx = 0
        m = 0
        for ch in correct_answers:
            if student_pattern[idx % len(student_pattern)] == ch:
                m += 1
            idx += 1
        return m

    No_of_exam_questions = 0
    Num_correct_questions = ""
    while True:
        Num_exam_questions = input("Enter No. of questions: ")
        if not (Num_exam_questions.isdigit()) or not (1 <= int(Num_exam_questions) <= 100):
            continue

        Num_exam_questions = int(Num_exam_questions)

        exam_answers = input("Enter correct questions: ")
        if not (exam_answers.isupper()) or len(exam_answers) != Num_exam_questions:
            continue
        break

    Adrian_grade = check_for_correct_answers(exam_answers, Adrian)
    Bruno_grade = check_for_correct_answers(exam_answers, Bruno)
    Goran_grade = check_for_correct_answers(exam_answers, Goran)

    all_students = {"Adrian": Adrian_grade, "Bruno": Bruno_grade, "Goran": Goran_grade}
    max_grade = max(all_students.values())
    print(max_grade)
    for student in all_students.keys():
        if all_students.get(student) == max_grade:
            print(student)


def numberfun():
    """
    1 <= N (test cases< <= 10000
        1 <= a,b,c <= 10000
        (a [-,+,*,/] b = c )
    :return:
    """

    def check_operation(num1, num2, num3):
        if abs(num1 - num2) == num3:
            return True
        elif num1 + num2 == num3:
            return True
        elif num1 * num2 == num3:
            return True
        elif num1 / num2 == num3 or num2 / num1 == num3:
            return True
        else:
            return False

    test_cases = 0

    a = b = c = 0
    while True:
        test_cases = input("Enter test cases: ")
        if not (test_cases.isdigit()) or not (1 <= int(test_cases) <= 10000):
            continue
        test_cases = int(test_cases)
        break

    while test_cases > 0:
        Numbers_a_b_c = input("Entrer info: ")
        if not ("".join(Numbers_a_b_c.split()).isdigit()):
            continue

        Numbers_a_b_c = Numbers_a_b_c.split()
        a = int(Numbers_a_b_c[0])
        b = int(Numbers_a_b_c[1])
        c = int(Numbers_a_b_c[2])
        if not (1 <= (a and b and c) <= 10000):
            continue

        if check_operation(a, b, c):
            print("Possible")
        else:
            print("Impossible")
        test_cases -= 1


def modulo():
    """
    use %42
    :return:
    """
    distinct_numbers = set()
    total_nums = 10
    for num in range(total_nums):
        while True:
            n = input()
            if not(0 <= int(n) <= 1000):
                continue
            n = int(n)

            mod_n = n % 42
            distinct_numbers.add(mod_n)
            break
    print(len(distinct_numbers))


def jobexpenses():
    """
    0 <= N (number Robin wrote down) <= 20000
        -50000 <= k(k != 0) <= 500000
    :return:
    """

    def check_expenses(exp_list):
        sum = 0
        exp_list = exp_list.split()
        if len(exp_list) != n_numbs:
            return False
        else:
            for amount in exp_list:
                if int(amount) == 0 or not(-50000 <= int(amount) <= 500000):
                    return False
                elif int(amount) < 0:
                    sum += abs(int(amount))
        return sum


    n_numbs = 0
    while True:
        n_numbs = input("How many numbers: ")
        if not(n_numbs.isdigit()) or not(0 <= int(n_numbs) <= 20000):
            continue

        n_numbs = int(n_numbs)
        break

    while True:
        expenses = input("Enter the expenses: ")
        sum_all = check_expenses(expenses)

        if sum_all is False:
            continue

        print(sum_all)
        break


def janitortroubles():
    """

    :return:
    """















