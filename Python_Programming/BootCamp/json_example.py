import json

"""
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None

"""

# some JSON string:
x = '{ "name":"John", "age":30, "city":"New York"}'


# parse x:
y = json.loads(x)

# print(y)
# the result is a Python dictionary:
print(y["name"])


# a Python object (dict):
x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Convert a Python object containing all the legal data types:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
