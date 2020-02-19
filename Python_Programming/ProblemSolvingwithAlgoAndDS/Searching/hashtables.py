class InvalidOperationException(Exception):
    pass


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


class HashTable:
    """
    to use quadratic probing change i to i*i
    """
    def __init__(self, tableSize=11):
        self.m = tableSize
        self.array = [None] * self.m
        self.n = 0

    def hash1(self, key):
        return key % self.m

    def rehash(self, new_size):
        temp = HashTable(new_size)
        for i in range(self.m):
            if self.array[i] is not None and self.array[i].get_student_id() != - 1:
                temp.insert(self.array[i])
        self.array = temp.array
        self.m = new_size

    def insert1(self, newRecord):
        if self.n >= self.m // 2:
            self.rehash((self.next_prime(2*self.m)))
            print("New table size is: ", self.m)
        self.insert(newRecord)

    def insert(self, newRecord):
        key = newRecord.get_student_id()
        h = self.hash1(key)

        location = h

        for i in range(1, self.m):
            if self.array[location] is None or self.array[location].get_student_id() == - 1:
                self.array[location] = newRecord
                self.n += 1
                return
            if self.array[location].get_student_id() == key:
                raise InvalidOperationException("Duplicate key")

            location = (h + i) % self.m

        print("Table is full: Record can't be inserted")

    def next_prime(self, x):
        while self.is_prime(x) is not True:
            x += 1
        return x
    
    def is_prime(self, x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    def search(self, key):
        h = self.hash1(key)
        location = h

        for i in range(1, self.m):
            if self.array[location] is None:
                return None
            if self.array[location].get_student_id() == key:
                return self.array[location]
            location = (h + i) % self.m
        return None

    def display_table(self):
        for i in range(self.m):
            print("[", end=""); print(i, end=""); print("]", end="");

            if self.array[i] is not None and self.array[i].get_student_id() != - 1:
                print(self.array[i])
            else:
                print("___")

    def delete(self, key):
        h = self.hash1(key)
        location = h

        for i in range(1, self.m):
            if self.array[location] is None:
                return None
            if self.array[location].get_student_id() == key:
                temp = self.array[location]
                self.array[location].set_student_id(-1)
                self.n -= 1
                return temp
            location = (h + i) % self.m

        return None


if __name__ == "__main__":
    size = int(input("Enter the size of the hash table: "))
    table = HashTable(size)

    while True:
        print("1. Insert record")
        print("2. Search record")
        print("3. Delete record")
        print("4. Display table")
        print("5. Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            id = int(input("Enter student id: "))
            name = input("Enter student name: ")
            record = studentRecord(id, name)
            table.insert(record)
        elif choice == 2:
            id = int(input("Enter an id to search: "))
            record = table.search(id)
            if record is None:
                print("Key is not found")
            else:
                print(record)
        elif choice == 3:
            id = int(input("Enter an id to delet: "))
            table.delete(id)
        elif choice == 4:
            table.display_table()
        elif choice == 5:
            break
        else:
            print("Wrong option")
        print("\n\n")
