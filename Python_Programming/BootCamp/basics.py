"""
int 3 200 300

float 3.0 200.0

str "hello"

list    [10,"hi", 33]

dict    {"money":"value"}  key:value relationship


"""
def myfunc(strng):
    result = strng[0].lower()
    for i in range(1, len(strng)):
        if i % 2 == 0:
            result += strng[i].lower()
        else:
            result += strng[i].upper()
    return result

print(1/2)
hello = "hello world"
s = "This is also a string"
tt = (10, "hey")
number = "2" + "3"
print(type(tt))
print(hello[::-1])
print(number)
print(type(number))
number = int(number)
print(type(number))
hello.capitalize()
print(hello)
print("This {q} {b} {f}".format(f="fox", b="brown", q="quick"))

result = 100/777
# {value:width.precision f}
# look into f strings
print("The result is: {r:5.2f}".format(r=result))

list1 = ["one", "one", "two", "hello", "hello"]
list1[0] = list1[0].upper()
print(list1)
#print(list1.pop(1))
print(list1)

first_dict = {"name":"Gonzalo", "Favorite food":"Pizza"}

print(first_dict['name'])
for k,v in first_dict.items():
    print(v)

t = ("a", "a", "a", "g", "o")
print(t.count("a"))

myset = set()
print(myset)
myset.add(1)
myset.add(2)
print(myset)
myset.add(1)
print(myset)
set(list1)
print(set(list1))
print(set("helo"))
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)
d = {'simple_key':'hello'}
print(d["simple_key"])
d2 = {'k1':{'k2':'hello2'}}
print(d2["k1"]["k2"])

# This will be hard and annoying!
d3 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello33']]}]}]}
print(d3["k1"][2]["k2"][1]["tough"][2][0])
nums = [1, 1, 1, 2, 3, 4]
print(sum(nums))
hh = "hello"
mhh = [letter for letter in hh]
print(mhh)
print(nums.count(1))
nums.reverse()
print(nums)
del nums[0]
print(nums)
print(myfunc("Anthropomorphism"))
player = (1, 2)
print(player[0])