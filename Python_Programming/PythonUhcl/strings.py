ss = "Hello, World!"
tt = ss

fruit = "banana"
list(enumerate(fruit))


def in_word(strng, ch):
	x = 0
	while x < len(strng):
		if strng[x] == ch:
			return x
		x += 1
	return -1

print(in_word("Computer", "t"))