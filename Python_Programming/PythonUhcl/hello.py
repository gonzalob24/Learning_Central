"""
import sys
print(sys.version)
x = 'Hello World'
s = 'This is my first program'
print(x + s)

# value = [5, 4, 3, 2, 1]
for i in range(1, 11):
    print (i, end=' ')


w = 100 / 3
z = 23 / 3


# formatted output
print("\nThe float rounder is %8.2f %8.2f" % (w, z))
"""

current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
print(final_time_int)
