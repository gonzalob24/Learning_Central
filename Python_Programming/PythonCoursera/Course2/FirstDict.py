
import string
string.punctuation  # ’!"#$%&\’()⋆+,-./:;<=>?@[\\]^_‘{|}~’

fname = input("Ente the name of the file: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
words = fhand.read()
#temp_d = words.__dict()
print(words)
'''
lst = words.split()
counts = dict()
for line in lst:
    counts[line] = counts.get(line, 0) + 1

print("Counts", counts)


word = "brontosaurus"

d= dict()

for c in word:
    d[c] = d.get(c, 0) + 1

print(d)
'''
