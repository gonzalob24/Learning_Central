# PRrogram to calculate overtime earnings
# and gross pay


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
overTime = h - 40
paywithOverTime = 0

if overTime > 0 :
    payWithOverTime = overTime * 1.5 * r 

payNoOverTime = (h - overTime) * r
    
print (payWithOverTime + payNoOverTime)