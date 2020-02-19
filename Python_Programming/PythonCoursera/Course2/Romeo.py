"""
Expected output in order
\
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', '
grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 
'window', 'with', 'yonder']



fname = input("Enter file name: ")
fh = open(fname)
lst = list()  #this is an empty list 
#print(fh.read())  #reads the file as it is written
for line in fh:
    split_line = line.rstrip().split()
    for word in split_line:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
"""

#for line in fh:
#    print(line.strip())


#10 most common word

fh = open("romeo.txt")
count = dict()
for line in fh:
    words = line.split()
    for w in words:
        count[w] = count.get(w, 0) + 1

list_two = list()
for k,v in count.items():
    list_two.append( (v,k) )

list_two = sorted(list_two,reverse = True)

for v,k in list_two:
    print(k, v)