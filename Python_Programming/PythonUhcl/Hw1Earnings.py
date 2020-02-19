#Weekly Pay: 
#Write a program that takes as inputs: 

#employee’s name, 
#hourly wage, 
#total regular hours and total overtime hours for the week. 
#After accepting the inputs for an employee your program 
#should calculate:
#total weekly pay (regular pay plus overtime pay) 

#for the employee. Overtime pay is calculated by multiplying overtime
#hours by 1.5 times the hourly wage. The program should then display 
#print) the name of the employee along with her/his total pay amount 
#for the week.

#ask user to i nout their name

name = input("what is your name: ")
hr_wage = float(input("What is your hourly wage: "))
total_hours_worked = float(input("How many hours did you work: "))


#calculate overtime
overt_time = total_hours_worked - 40
over_time_pay = 0
if overt_time > 0:
	over_time_pay = overt_time * 1.5 * hr_wage

total_weekly_Pay = (total_hours_worked - overt_time) * hr_wage + over_time_pay

print(name + " has earned $" + str(total_weekly_Pay) + " dollars for the week.")
