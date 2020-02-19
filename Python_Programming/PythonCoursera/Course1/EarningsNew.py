# PRrogram to calculate overtime earnings
# and gross pay


hrs = input("Enter Hours:")
rate = input("Enter rate:")

while True:
	try:
		h = float(hrs)
		r = float(rate)
	except:
		print("Error, please enter numeric input")
		quit()
	
overTime = h - 40

if overTime > 0 :
    payWithOverTime = overTime * 1.5 * r 
    payNoOverTime = (h - overTime) * r
else :
	payNoOverTime = (h - overTime) * r
    
print (payWithOverTime + payNoOverTime)