import math

print(math.ceil(6/5))
print(7//8)
arr = [1,2,3,4,11,21]
print(max([1,2,3,4,11,21]))

arr.append(22)
arr.insert(0,44)
print(max(arr))
print(arr.pop(0))
print(arr)

arr1  = [1, 4, 2, 3, 5]
mm = map(lambda x: str(x), arr1)
print(list(mm))
for c in "Gonzalo":
  print(c)

d = {}

if not d.get('me'):
  print('Nope')