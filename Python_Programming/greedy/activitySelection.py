class Info:
    def __init__(self, name, start, finish):
        self.name = name
        self.start = start
        self.finish = finish


class Activities:
    def __init__(self):
        self.activitiesList = []

    def add_activity(self, name, start, finish):
        tempActivity = Info(name, start, finish)
        index = 0
        if len(self.activitiesList) == 0:
            self.activitiesList.append(tempActivity)
        else:
            for activity in self.activitiesList:
                if tempActivity.finish < activity.finish:
                    self.activitiesList.insert(index, tempActivity)
                    break
                    # index += 1
                index += 1
            if tempActivity not in self.activitiesList:
                self.activitiesList.append(tempActivity)

    def max_activities(self):
        max_count = 1
        # start with first activity
        prevActivity = self.activitiesList[0]

        # start at the second activity and compare with previous activity
        for index in range(1, len(self.activitiesList)):
            currentActivity = self.activitiesList[index]
            # compare previous activity finish time with current activity start time
            if prevActivity.finish < currentActivity.start:
                max_count += 1
                # update previous activity if I do it
                prevActivity = currentActivity

        return max_count

    def display(self):
        for activity in self.activitiesList:
            print(
                f'{activity.name}: start: {activity.start} finish: {activity.finish}')


a = Activities()
a.add_activity("A1", 0, 6)
a.add_activity("A2", 3, 4)
a.add_activity("A3", 1, 2)
a.add_activity("A4", 5, 8)
a.add_activity("A5", 5, 7)
a.add_activity("A6", 8, 9)
a.display()
print("Max Activities: ", a.max_activities())
# test = [6]
# print(test)
# test.insert(0, 4)
# test.insert(0, 2)

# print(test)
