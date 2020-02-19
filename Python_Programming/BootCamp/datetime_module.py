import datetime
import timeit

t = datetime.time(5, 25, 10)

print(t)
print(t.min)
print(t.max)
print(t.resolution)
print(t.minute)

today = datetime.date.today()
print(today)

print(today.timetuple())
print(today.year)
print(datetime.date.min)

# 0-1-2-3-4-5...-99
print("First time:")
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
print("\nLets make it a list comprehension:")
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
print("\nUsing map")
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))

