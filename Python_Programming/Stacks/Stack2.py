# Better implementation of the stack


class StackEmptyError(Exception):
    pass


class StackFullError(Exception):
    pass


class Stack:
    # In this implementation of the stack we cannot use the
    # append and pop methods since stack is not empty to begin with

    def __init__(self, max_size=10):
        self.items = [None] * max_size  # Here the stack does not start out empty
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0  # If the count is 0 then stack is empty, it has no values

    def is_full(self):
        return self.count == len(self.items)

    def push(self, value1):
        if self.is_full():
            return StackFullError("Stack is full, can't push")

        self.items[self.count] = value1
        self.count += 1

    def pop(self):
        if self.is_empty():
            return StackFullError("Stack is empty, can't pop")

        x = self.items[self.count - 1]
        self.items[self.count - 1] = None
        self.count -= 1

        return x  # returns the value that we are removing

    def peek(self):
        if self.is_empty():
            return StackFullError("Stack is empty, nothing to peek")

        return self.items[self.count - 1]

    def display(self):
        print(self.items)
# 346-349-8948 10am

if __name__ == '__main__':
    brackets = "(({{[[]]}}))"
    bb2 = ')(()){([()])}'
    b3 = '[][][]{}{}()()'
    left = "({["
    right = ")}]"
    def is_valid(expression):
        stack = Stack(max_size=13)

        def match(left, right):
            if left == '[' and right == ']':
                return True
            elif left == '(' and right == ')':
                return True
            elif left == '{' and right == '}':
                return True
            else:
                return False

        for parenthesis in expression:
            if parenthesis in left:
                stack.push(parenthesis)
            else: # parenthesis in right
                if stack.is_empty():
                    print("Right parenthesis are greater than left")
                    return False
                else:
                    popped_parenthesis = stack.pop()
                    if not match(popped_parenthesis, parenthesis):
                        print("Mismathed parenthesis are {} and {}".format(parenthesis, popped_parenthesis))
                        return False
        
        if stack.is_empty():
            print("Balance Parenthesis")
            return True
        else:
            print("Left side is greater. Parenthesis not balanced.")
            return False

    print(is_valid(b3))  

    while False:
        print('1.Push')
        print('2.Pop')
        print('3.Peek')
        print('4.Size')
        print('5.Display')
        print('6.Quit')

        option = int(input("Enter an option: "))

        if option == 1:
            data = int(input("Enter the value you want to push: "))
            stack1.push(data)
        elif option == 2:
            value = stack1.pop()
            print('The value popped was ', value)
        elif option == 3:
            value = stack1.peek()
            print('The value peeked was ', value)
        elif option == 4:
            value = stack1.size()
            print('The size of the stack is ', value)
        elif option == 5:
            stack1.display()
        elif option == 6:
            break
        else:
            print('Invalid option, pick again')
