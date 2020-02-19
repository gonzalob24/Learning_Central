# Using the text file studentdata.txt write a program that prints out the names of
# students that have more than six quiz scores.

fname = open('studentdata.txt', 'r')


def quizes(fname):
    for line in fname:
        items = line.split()
        #print(items)
        if len(items[1:]) > 6:
            print(items[0])
    fname.close()

#quizes(fname)

# Problem 2
# Using the text file studentdata.txt (shown in exercise 1) write a program that
# calculates the average grade for each student, and print out the student’s name
# along with their average grade.

def average(fname):
    avg = 0
    for line in fname:
        items = line.split()
        print(items[0], end=" ")
        sum = 0
        for n in range(len(items[1:])):
            sum += int(items[n + 1])
            avg = sum / len(items[1:])
        print('{0:.2f}'.format(avg))
    fname.close()

average(fname)
