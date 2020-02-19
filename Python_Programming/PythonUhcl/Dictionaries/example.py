eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

eng22sp = {'one':'uno', 'two':'dos', 'three':'tres'}

one_dict_keys = eng2sp.keys()
one_list_keys = list(eng2sp.keys())

print(one_list_keys)
print(len(eng2sp))
print(eng2sp)
print(eng22sp)

print("Another example")

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)

print("------")
print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)


print("_____")
for k in inventory:
    print("Got", k, "that maps to", inventory[k])


print("_____")
print("get method for dictionaries")

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))
