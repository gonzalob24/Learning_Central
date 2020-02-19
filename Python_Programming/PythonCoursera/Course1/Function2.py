count = 0
total = 0
average = 0
smallest = None
largest = None
while True:
	number = input("Enter a number: ")
	if number == 'done':
		break
	try:
		num = int(number)
	except:
		print("Error enter a numeric value")
		continue
	if smallest is None :
		smallest = num
		largest = num
	elif num < smallest :
		smallest = num
	elif num > largest :
		largest = num

	count = count + 1
	total = total + num
	average = float(total / count)

print(count, total , average, smallest, largest)