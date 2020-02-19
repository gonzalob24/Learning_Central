class MyTime:

    def __init__(self, hrs=0, mins=0, sec=0):
        """ Create a MyTime object initialized to hrs, mins, secs """

        totalsecs = hrs * 3600 + mins * 60 + sec
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

    def increment(self, seconds):
        self.seconds += seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def to_seconds(self):
        """ Return the number of seconds represented by this instance """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())
    """
    def after(self, time2):
        Return True of I am strictly greater than time2
            We can make the if stmts easier to read and implement
        if self.hours > time2.hours:
            return True
        if self.hours < time2.hours
            return False

        if self.minutes > time2.minutes:
            return True
        if self.minutes < time2.minutes:
            return False

        if self.seconds > time2.seconds:
            return True
        else:
            return False 
        return self.to_seconds() > time2.to_seconds()
    """
    def between(self, other1, other2):
        return other1.to_seconds() < self.to_seconds() < other2.to_seconds()

    # Overload the necessary operator(s) so that instead of having to write
    # if t1.after(t2): ...
    # we can use the more convenient
    # if t1 > t2: ...
    def __gt__(self, time_two):
        return MyTime(0, 0, self.to_seconds() > time_two.to_seconds())


# def add_time(tt1, tt2):
    #secs = tt1.to_seconds() + tt2.to_seconds()
    #return MyTime(0, 0, secs)


# Instantiate an object
time1 = MyTime(11, 59, 35)
current_time = MyTime(9, 14, 30)
bread_time = MyTime(20, 35, 50)
current_time.increment(500)
# done_time = add_time(current_time, bread_time)
current_time.increment(500)
# print(done_time)

print("Using the def __add__ method")

t1 = MyTime(5, 0, 0)
t2 = MyTime(3, 50, 30)
t3 = t1 + t2
print("+ ")
print(t3)
print("after")
#print(time1.after(t2))
if t1.__gt__(t2):
    print("True")
print("second after")
if t1 > t2:
    print("working")
print(t1.__add__(t2)) # this style is more elegant
print("between")
print(time1.between(t1, t2))
