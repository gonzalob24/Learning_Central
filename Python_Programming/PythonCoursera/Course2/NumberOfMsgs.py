#Write a program to read through the mbox-short.txt and figure out who
#has sent the greatest number of mail messages. The program looks for
#'From ' lines and takes the second word of those lines as the person who
#sent the mail. The program creates a Python dictionary that maps the
#sender's mail address to a count of the number of times they appear in
#the file. After the dictionary is produced, the program reads through the
#dictionary using a maximum loop to find the most prolific committer.


name = input("Enter file: ")

if len(name) < 1:
	name = "mbox-short.txt"

handle = open(name)
max_val = 0
theword = None
#print(handle.read()) reads the file
email = dict()
for line in handle:
	if line.startswith("From "):
		line = line.split()
		word = line[1:2]
		#print(word)
		for w in word:
			email[w] = email.get(w, 0) + 1
for k, v in email.items():
	#print(k, v)
	if v > max_val:
		max_val = v
		theword = k
print(theword, max_val)


d




