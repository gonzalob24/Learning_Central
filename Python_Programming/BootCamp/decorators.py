def hi(name="Joe"):
    print("The hi() function has been executed.")

    def greet():
        return "\t this is the greet() function inside hi"

    def welcome():
        return "\t this is the welcome() function inside hi"

    print("I will return a function")

    if name =="Joe":
        return greet()
    else:
        return welcome()


def hello():
    return "Hi G!"


def other(some_func):
    print("Other code runs here")
    print(some_func())  # executes the function


def original_decorator(original_fun):

    def wrap_function():
        print("Some code before original function")

        original_fun()

        print("Some code after original function")

    return wrap_function


# apply the decorator to the new function
@original_decorator
def function_needs_decorator():
    print("I need to be decorated")


#decorated_function = original_decorator(function_needs_decorator)
#decorated_function()

function_needs_decorator()
