"""
In python: Using the TXBabyNames.txt file.
Write code to read it into a list.

How many female records are there? Done
How many male records are there? Done

How many female records are there in 1910? Done
How many male records are there in 1910? Done

How many female records are there in 2012? Done
How many male records are there in 2012? Done

What are the total number of babies born in Texas in 2012? Done

What are the total number of babies born in Texas with your name since 1910? Done

What are the total number of babies born in Texas with your name between 1910 and 1960? Done

What name was the most popular (had the highest count in one year) for males? Done
What name was the most popular (had the highest count in one year) for females? Done

What was the name for the males, and for the females? Done

What year was the name for males? for females? Done

In what year was your name the most popular (had the highest count)?
Example name: Paul

Write all this information out to a file.

"""
file_names = open("TXBabyNames.txt")
# open_now = file_names.readline()
# open_now = file_names.readlines() puts entire file in a list
# read reads all of it
# reaadline just reads the firts line
# print(open_now)

# to read line by line do a for loop
female_sum = 0
male_sum = 0
female_sum_1910 = 0
male_sum_1910 = 0
female_sum_2012 = 0
male_sum_2012 = 0
tx_babies_2012 = 0
tx_babies_myname = 0
tx_babies_myname_1910_1960 = 0
popular_male_count = 0
popular_male_name = ""
popular_male_name_year = 0
popular_female_count = 0
popular_female_name = ""
popular_female_name_year = 0
popular_myname_count = 0
popular_myname_year = 0

for line in file_names:
    line = line.split(",")

    # total number of females
    if line[1] == "F":
        female_sum += int(line[4])

    # total number of males
    if line[1] == "M":
        male_sum += int(line[4])

    # total females in 1910
    if int(line[2]) == 1910 and line[1] == "F":
        female_sum_1910 += int(line[4])

    # total male records in 1910
    if int(line[2]) == 1910 and line[1] == "M":
        male_sum_1910 += int(line[4])

    # total females in 2012
    if int(line[2]) == 2012 and line[1] == "F":
        female_sum_2012 += int(line[4])

    # total male records in 2012
    if int(line[2]) == 2012 and line[1] == "M":
        male_sum_2012 += int(line[4])

    # babies born in TX in 2012
    if line[0] == "TX" and int(line[2]) == 2012:
        tx_babies_2012 += int(line[4])

    # TX babies born since 1910 with my name
    if line[0] == "TX" and line[3] == "Ira":
        tx_babies_myname += int(line[4])

    # TX babies with my name between 1910 and 1960
    if line[0] == "TX" and line[3] == "Gonzalo" and int(line[2]) in range(1910, 1961):
        tx_babies_myname_1910_1960 += int(line[4])

    # most popular male name in one year
    if line[1] == "M":
        if popular_male_count < int(line[4]):
            popular_male_count = int(line[4])
            popular_male_name = line[3]
            popular_male_name_year = line[2]

    # most popular female name in one year
    if line[1] == "F":
        if popular_female_count < int(line[4]):
            popular_female_count = int(line[4])
            popular_female_name = line[3]
            popular_female_name_year = line[2]

    # most popular year for my name
    if line[3] == "Gonzalo":
        if popular_myname_count < int(line[4]):
            popular_myname_count = int(line[4])
            popular_myname_year = line[2]

print("There are a total of " + str(female_sum) + " female records.")
print("There are a total of " + str(male_sum) + " male records.")
print("There are a total of " + str(female_sum_1910) + " female records in 1910.")
print("There are a total of " + str(male_sum_1910) + " male records in 1910.")
print("There are a total of " + str(female_sum_2012) + " female records in 2012.")
print("There are a total of " + str(male_sum_2012) + " male records in 2012.")
print("There are a total of " + str(tx_babies_2012) + " Babies born in TX in 2012.")
print("There are a total of " + str(tx_babies_myname) + " Babies born in TX in 1910 with my name.")
print("There are a total of " + str(tx_babies_myname_1910_1960) +
      " Babies born in TX with my name from 1910 to 1960.")
print("The most popular male name in a given year is " + popular_male_name + ". There were " + str(popular_male_count) +
      " in " + popular_male_name_year)
print("The most popular female name in a given year is " + popular_female_name + ". There were " + str(popular_female_count) + " in " + popular_female_name_year)
print("The year that my name was most famous was in " + popular_myname_year + ". There were " + str(popular_myname_count))
