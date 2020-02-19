class EmptyStackError(Exception):
    pass


class Stack:

    # Constructor you can start with an empty list
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  # Pop is used to remove the last element from the list
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[-1]

    def display(self):
        print(self.items)


if __name__ == "__main__":
    st = Stack()   # I can add up to 10 elements since 10 is tha max size

    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Display")
        print("6. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            x = int(input("Enter the element to be pushed: "))
            st.push(x)
        elif choice == 2:
            x = st.pop()
            print("Popped element is: ", x)
        elif choice == 3:
            print("Element at the top is: ", st.peek())
        elif choice == 4:
            print("Sie of stack is: ", st.size())
        elif choice == 5:
            st.display()
        elif choice == 6:
            break
        else:
            print("Wrong choice")
        print()


