from collections import defaultdict

# a defaultdict will never raise a KeyError.
# Any key that does not exist gets the valye
# returned by the default factory

d = {"k1": 1}
print(d["k1"])
# print(d["k2"])

# pass in object
d2 = defaultdict(object)

# print(d2["one"])

for item in d2:
    print(item)

# We can use this to initialize default values
# in conjunction with a lambda function

d3 = defaultdict(lambda: 0)
d3["one"]
d3["two"] = 2

print(d3)
