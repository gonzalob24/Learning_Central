import collections as col
def transformArray(arr):
    newArr = [None] * len(arr)
    newArr[0], newArr[-1] = arr[0], arr[-1]

    change = True
    while(change):
        for i in range(1, len(arr) - 1):
            if (arr[i - 1] > arr[i] < arr[i + 1]):
                newArr[i] = arr[i] + 1
            elif(arr[i - 1] < arr[i] > arr[i + 1]):
                newArr[i] = arr[i] -  1
            else:
                newArr[i] = arr[i]
            
        if newArr == arr:
            return newArr
        arr = newArr.copy()


s = 'Gonzalo'

if 'G' in s:
    s.replace('G','')

c = col.Counter(s).values()
print(c)
arr = [2,7,11,5]
for i, num in enumerate(arr):
    print(i, num)

def twoSUm(nums, target):
    hash_n = {}

    for i, num in enumerate(nums):
        n = target - num
        if n not in hash_n:
            hash_n[num] = i
        else:
            return [hash_n[n], i]

print(twoSUm([3,5,-4,8,11,1,-1,6], 10))

print('--------Logger----------')
from collections import deque

message = set()
msg_queue = deque()
message.add('foo')
msg_queue.append(('foo', 2))
msg_queue.append(('bar', 7))
print(message)
print(msg_queue)

