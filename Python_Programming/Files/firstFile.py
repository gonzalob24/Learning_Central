# Using the text file studentdata.txt write a program that prints out the names of
# students that have more than six quiz scores.

fname = open('studentdata.txt', 'r')
txt = fname.readline()
for line in fname:
    items = line.split()
    #print(items)
    if len(items[1:]) > 6:
        print(items[0])
fname.close()

