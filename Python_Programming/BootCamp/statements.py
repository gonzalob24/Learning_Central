# Use for, .split(), and if to create a Statement that will print out
# words that start with 's':

st = 'Print only the words that start with s in this sentence'

for ch in st.split():
    if ch.startswith("S".lower()):
        print(ch)

    if len(ch) % 2 == 0:
        print("Length of \"{}\" is even".format(ch))

my_odds = [ x for x in range(1, 51) if x % 3 == 0]
print(my_odds)
