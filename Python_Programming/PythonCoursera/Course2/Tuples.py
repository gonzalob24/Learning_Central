d = {"a": 10, "e": 1, "c": 22, "b": 5}
t = d.items()
print(t)
# for k, v in sorted(t):
#    print(k, v)
for i in d:
    print(i, d[i])
# Sorting the tuples bases on the value and not the key
temp_list = list()  # create an empty list and will append the value a key from the dict()

for k, v in t:
    temp_list.append((v, k))

print(sorted(temp_list, reverse=True))
