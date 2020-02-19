num = 0
total = 0.0

while True:
	sval = input("Enter a number: ")
	if sval == "done":
		break
	try:
		fval = float(sval)
	except:
		print("Invalid Input")
		continue #go back to the top of the loop
	#print(fval)
	num = num + 1
	total = total + fval

print("ALL DONE")
print(total, num, total/num)
