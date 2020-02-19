#Write a program that prompts for a file name, then opens 
#that file and reads through the file, looking for lines 
#of the form: X-DSPAM-Confidence:    0.8475

#Count these lines and 
#extract the floating point values 
#from each of the lines and compute the average of those 
#values and produce an output as shown below. 

#Do not use the sum() function or a variable named sum 
#in your solution. when you are testing below enter 
#Average spam confidence: 0.750718518519
#mbox-short.txt as the file name.

fileName = input('Enter the name of the file: ')

fileOpen = open(fileName)
count = 0
average = 0
intPosition = 0
for line in fileOpen :
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	position = line.find("0")
	intPosition += float(line[position:])
	count += 1
	average = intPosition / count

print("Average spam confidence: ", float(average))

#print(fileOpen.read())