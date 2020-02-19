
class Animals():

    def __init__(self, type_of_animal, color):
        self.type_of_animal = type_of_animal
        self.color = color

    def eat(self, food_type):
        return "my {0} likes to eat {1}".format(self.type_of_animal, food_type)
