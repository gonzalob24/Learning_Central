from Animals import Animals


class Dog(Animals):
    # CLASS OBJECT ATTRIBUTE is THE SAME INSTANCE OF A CLASS
    species = "mammal"

    # Dogs have attributes or characteristics
    # constructor for the class
    # Self refers to the instance itself, the object we are talking about
    def __init__(self, type_of_animal, color, name):  # self connects to the instance of the class
        Animals.__init__(self, type_of_animal, color)
        # spots is a boolean True/False
        self.color = color
        self.breed = type_of_animal
        self.name = name


    def bark(self, number):
        print("WOOF! My name is {} and the number is {}.".format(self.name, number))



my_dog = Dog("Wolf", "Canelo", "Black")
print(my_dog.species)
my_dog.bark(21)
print(type(my_dog))
print(my_dog.eat("Kibbles"))

print(my_dog.breed)
mylist = [1,2,3]

print(mylist.__add__([1,2,3]))
print(mylist)
