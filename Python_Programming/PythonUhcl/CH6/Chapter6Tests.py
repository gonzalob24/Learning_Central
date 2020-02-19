import sys

def test(did_pass):
	linenum = sys._getframe(1).f_lineno
	if did_pass:
		msg = "Test at line {0} ok.".format(linenum)
	else:
		msg = "Test at line {0} FAILED.".format(linenum)
	print(msg)

#test suite will make a few tests to assert the values
#I will be adding tests as I make additional exercices. 
def test_suite():
	test(turn_clockwise("N") == "E")
	test(turn_clockwise("W") == "N")
	test(turn_clockwise(42) == None)
	test(turn_clockwise("rubbish") == None)
	print()
	test(day_name(3) == "Wednesday")
	test(day_name(6) == "Saturday")
	test(day_name(42) == None)
	print()
	test(day_num("Friday") == 5)
	test(day_num("Sunday") == 0)
	test(day_num(day_name(3)) == 3)
	test(day_name(day_num("Thursday")) == "Thursday")
	test(day_num("Halloween") == None)


#that takes one of these four compass points as its parameter, 
#and returns the next compass point in the clockwise direction
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
		return None

#day_name that converts an integer number 0 to 6 into the name of a day
#Assume day 0 is “Sunday”. Once again, return None if the arguments
#to the function are not valid
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

#Write the inverse function day_num which is given a day name, and returns its number:
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

#run tests
test_suite()