# Write a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages. You can pull the hour out from the
#'From ' line by finding the time and then splitting the string a second
# time using a colon.
#           From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.


file_open = open("mbox-short.txt")

hour_dict = dict()

for line in file_open:
    if line.startswith("From "):
        line = line.rstrip().split()
        hour = line[5].split(":")
        new_hour = hour[0]
        hour_dict[new_hour] = hour_dict.get(new_hour, 0) + 1

lst = list()
for k, v in hour_dict.items():
    lst.append((k, v))

temp_lst = sorted(lst)
# print(lst)
for k, v in temp_lst:
    print(k, v)
