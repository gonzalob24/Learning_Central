""" Open the file mbox-short.txt and read it line by line. When you find a 
line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second 
word in the line (i.e. the entire address of the person who sent the message). 
Then print out a count at the end.

Hint: make sure not to include the lines that start with 'From:'.

"""

fname = input("Enter file name: ") #input the name of the file
if len(fname) < 1 : 
    fname = "mbox-short.txt"

fh = open(fname) #open the file
count = 0        # start a counter
for line in fh:
    line = line.rstrip()
    word = line.split()
    #print("Line:", line)
    #print("word:", word)
    #print(len(word))
    #Guardian pattern checks to see if a list is empty is so it will skip it
    if len(word) < 1 or word[0] != 'From':  #looking for the from. Short circuit evaluation
        continue 
    count = count + 1                            
    print(word[1])
print("There were", count, "lines in the file with From as the first word")

