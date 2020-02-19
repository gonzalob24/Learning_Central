class studentRecord:

    def __init__(self, i, name):
        self.studentID = i
        self.studentName = name

    def get_student_id(self):
        return self.studentID

    def set_student_id(self, i):
        self.studentID = i

    def __str__(self):
        return str(self.studentID) + " " + self.studentName


class Node:

    def __init__(self, info, next=None):
        self.info = info
        self.next = next

